from pathlib import Path

# base folder where the instagram images live
base = Path("archive/images/posts")

# collect all jpg/png/webp images under posts/
paths = sorted(
    p for p in base.rglob("*")
    if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}
)

print('::: {layout-ncol=3}\n')

for p in paths:
    rel_path = p.as_posix()
    # simple alt text; you can edit later if you want
    print(f'![]({rel_path})' + '{fig-alt="Nepenthes"}\n')

print(":::")

