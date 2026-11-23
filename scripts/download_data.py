"""Download the UCI Online News Popularity dataset into data/OnlineNewsPopularity.csv."""
import io
import urllib.request
import zipfile
from pathlib import Path

URL = "https://archive.ics.uci.edu/static/public/332/online+news+popularity.zip"
OUT = Path(__file__).resolve().parent.parent / "data" / "OnlineNewsPopularity.csv"


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    raw = urllib.request.urlopen(URL, timeout=120).read()
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        name = [n for n in z.namelist() if n.endswith(".csv")][0]
        OUT.write_bytes(z.read(name))
    print(f"Saved {OUT} ({OUT.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
