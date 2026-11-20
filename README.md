# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/nimonandang15/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/nimonandang15/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image that sums up the world's news of Friday 20 November 2026 — a newspaper front page, "The World in One Day", with the six stories that defined the day.

## The day's news

1. **Trump, Xi & Putin meet face to face** — the first-ever three-way summit, in Shenzhen, ends with a joint declaration to cut nuclear risk, but no breakthrough on Ukraine or Iran.
2. **Myanmar guilty of genocide** — the World Court rules the army sought to destroy the Rohingya in its 2017 crackdown.
3. **Cyclone Akvan nears Odisha** — 300,000 evacuated as the severe cyclone closes schools and trains; 423 rescue teams deployed.
4. **Anthropic's record IPO** — $81.3bn raised; shares close 17% up on debut.
5. **Iran decision put off to 2027** — Trump says there is "no rush" on war.
6. **Voyager 1 passes a light-day** — NASA confirms the probe is a full light-day from Earth, a first for any spacecraft.

Sources: Reuters, BBC, The Hindu, Times of India — 20 Nov 2026.

`main.ts` (Node 22, standard library only) copies `entry.png` byte for byte to `/output/entry.png`, refusing anything that is not a whole PNG within the gate limits (≤ 1 MiB, ≤ 1024×1024). Both runs write the same bytes. The poster is drawn by `render.py` (PIL + DejaVu only).

## Run it

```sh
python3 render.py            # rebuild entry.png (deterministic)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=cydbk12s&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
