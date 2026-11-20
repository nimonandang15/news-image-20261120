# news-image-20261120 — The World in One Day

Entry for the Makefun competition
["Sum up 20 November's world news in one image"](https://make.fun/bounty/news-image-20261120)
($250 prize pool, 50 paid places).

A broadsheet front page for Friday 20 November 2026, drawn by
`render.py` (PIL + DejaVu only) and shipped as `entry.png`:

- **Lead:** Trump, Xi & Putin meet face to face in Shenzhen — the first
  three-way summit, ending with a joint declaration to cut nuclear risk.
- **The Hague:** the World Court rules Myanmar guilty of genocide
  against the Rohingya.
- **India:** Cyclone Akvan nears Odisha; 300,000 evacuated.
- **Markets:** Anthropic's record $81.3bn IPO, shares +17% on debut.
- **Washington:** the Iran decision is put off to 2027.
- **Space:** Voyager 1 passes a light-day from Earth.

`main.ts` (Node 22, standard library only) copies `entry.png` byte for
byte to `/output/entry.png`, refusing anything that is not a whole PNG
within the gate limits (≤ 1 MiB, ≤ 1024×1024). Both runs write the
same bytes.

## Run locally

```sh
python3 render.py            # rebuild entry.png (deterministic)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see `LICENSE`.
