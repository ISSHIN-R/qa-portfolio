from pathlib import Path

folder = Path(__file__).parent
files = [(p.name, p.stat().st_size) for p in folder.iterdir() if p.is_file()]
files.sort(key=lambda item: item[1], reverse=True)

print(f"文件夹：{folder}")
print(f"共 {len(files)} 个文件\n")

for name, size in files:
    print(f"{size:>8,} 字节    {name}")