#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SOCKS7 contribution generator
-----------------------------
Builds an animated "network packet" contribution graph for a GitHub profile.
It is intentionally NOT a clone of github-readme-stats: every cell is a node
on a SOCKS7 fabric, drawn with a hand-written palette and SVG animations.

Usage:
    GITHUB_TOKEN=xxx GITHUB_LOGIN=yourname python3 scripts/generate_contribution.py
Env (all optional):
    GITHUB_LOGIN   -> profile login (default: reads from OWNER or 'socks7-v2rei')
    OUT            -> output svg path (default: assets/contribution-network.svg)
    ACCENT         -> hex accent used for the hottest level
"""

import os
import json
import random
import datetime
import urllib.request

LOGIN = os.environ.get("GITHUB_LOGIN") or os.environ.get("OWNER") or "socks7-v2rei"
TOKEN = os.environ.get("GITHUB_TOKEN")
OUT = os.environ.get("OUT", "assets/contribution-network.svg")
ACCENT = os.environ.get("ACCENT", "#00f0ff")

API = "https://api.github.com/graphql"
QUERY = """
query($login:String!){
  user(login:$login){
    contributionsCollection{
      contributionCalendar{
        totalContributions
        weeks{ contributionDays{ date contributionCount weekday } }
      }
    }
  }
}
"""

# ---- SOCKS7 palette (level 0 .. 4) -----------------------------------------
LEVELS = ["#101d33", "#123a52", "#11618a", "#00a7c4", ACCENT]


def fetch_weeks():
    """Return (total, weeks[list[list[(date, count, weekday)]]])."""
    if TOKEN:
        payload = json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode()
        req = urllib.request.Request(
            API,
            data=payload,
            headers={
                "Authorization": "bearer %s" % TOKEN,
                "Content-Type": "application/json",
                "User-Agent": "socks7-profile",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                data = json.loads(r.read().decode())
            cal = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]
            weeks = []
            for w in cal["weeks"]:
                days = []
                for d in w["contributionDays"]:
                    days.append((d["date"], d["contributionCount"], d["weekday"]))
                weeks.append(days)
            return cal["totalContributions"], weeks
        except Exception as e:  # noqa: BLE001
            print("! live fetch failed (%s); falling back to synthetic data" % e)

    # ---- synthetic fallback so the SVG always renders -----------------------
    random.seed(7)
    today = datetime.date.today()
    start = today - datetime.timedelta(days=364)
    start -= datetime.timedelta(days=(start.weekday() + 1) % 7)  # align to Sunday
    weeks, total, day = [], 0, start
    while day <= today:
        week = []
        for _ in range(7):
            if day > today:
                week.append((day.isoformat(), 0, (day.weekday() + 1) % 7))
            else:
                c = random.choice([0, 0, 1, 2, 3, 4, 7, 11, 0, 2, 5, 0])
                total += c
                week.append((day.isoformat(), c, (day.weekday() + 1) % 7))
            day += datetime.timedelta(days=1)
        weeks.append(week)
    return total, weeks


def level(count):
    if count == 0:
        return 0
    if count <= 2:
        return 1
    if count <= 5:
        return 2
    if count <= 9:
        return 3
    return 4


def build_svg(total, weeks):
    cell, gap = 12, 3
    step = cell + gap
    pad_l, pad_t = 26, 74
    w = pad_l * 2 + len(weeks) * step
    h = pad_t + 7 * step + 46

    parts = []
    a = parts.append
    a('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="100%%" height="%d" '
      'role="img" aria-label="SOCKS7 contribution network">' % (w, h, h))
    a('<defs>')
    a('<linearGradient id="cnet" x1="0" y1="0" x2="1" y2="0">'
      '<stop offset="0" stop-color="#00f0ff"/><stop offset="0.5" stop-color="#8a5cff"/>'
      '<stop offset="1" stop-color="#ff2fd0"/></linearGradient>')
    a('<filter id="cglow" x="-60%" y="-60%" width="220%" height="220%">'
      '<feGaussianBlur stdDeviation="2.6" result="b"/>'
      '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    swp = len(weeks) * step
    a('<style>'
      '.cn{font-family:ui-monospace,"JetBrains Mono","SF Mono",Menlo,Consolas,monospace}'
      '@keyframes tw{0%,100%{opacity:.35}50%{opacity:1}}'
      '.tw{animation:tw 2.6s ease-in-out infinite}'
      '@keyframes swp{from{transform:translateX(0)}to{transform:translateX(' + str(swp) + 'px)}}'
      '.swp{animation:swp 9s linear infinite}'
      '</style>')
    a('</defs>')
    a('<rect width="%d" height="%d" fill="#060a12"/>' % (w, h))

    # header
    a('<text x="26" y="34" class="cn" font-size="13" fill="#cfe4ff" letter-spacing="2">'
      '// SOCKS7 FABRIC · CONTRIBUTION PACKETS</text>')
    a('<text x="%d" y="34" text-anchor="end" class="cn" font-size="12" fill="#5fd0ff">'
      '%s · %s total</text>' % (w - 26, LOGIN, format(total, ",")))
    a('<line x1="26" y1="46" x2="%d" y2="46" stroke="#152743"/>' % (w - 26,))

    # weekday gutter
    for idx, lbl in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
        a('<text x="6" y="%d" class="cn" font-size="9" fill="#40598a">%s</text>'
          % (pad_t + idx * step + 9, lbl))

    # cells
    anim_slots = set()
    rnd = random.Random(11)
    for wx, week in enumerate(weeks):
        for day in week:
            _, count, wd = day
            lv = level(count)
            x = pad_l + wx * step
            y = pad_t + wd * step
            extra = ""
            if lv >= 3 and rnd.random() < 0.35:
                anim_slots.add((wx, wd))
                extra = ' class="tw" style="animation-delay:%.1fs"' % (rnd.random() * 2.6)
            glow = ' filter="url(#cglow)"' if lv == 4 else ""
            a('<rect x="%d" y="%d" width="%d" height="%d" rx="3.5" fill="%s"%s%s/>'
              % (x, y, cell, cell, LEVELS[lv], glow, extra))

    # sweeping scan column
    a('<g class="swp" opacity="0.5"><rect x="%d" y="%d" width="2" height="%d" fill="url(#cnet)"/>'
      '</g>' % (pad_l, pad_t - 6, 7 * step + 12))

    # legend (right-aligned, kept fully inside the canvas)
    more_x = w - 52
    sw_end = more_x - 34
    sw_start = sw_end - 5 * step
    less_x = sw_start - 34
    ly = h - 30
    a('<text x="%d" y="%d" class="cn" font-size="10" fill="#5a7096">less</text>'
      % (less_x, ly + 11))
    for i, c in enumerate(LEVELS):
        a('<rect x="%d" y="%d" width="%d" height="%d" rx="3" fill="%s"/>'
          % (sw_start + i * step, ly, cell, cell, c))
    a('<text x="%d" y="%d" class="cn" font-size="10" fill="#5a7096">more</text>'
      % (more_x, ly + 11))
    a('<text x="26" y="%d" class="cn" font-size="11" fill="#3fe0a0">'
      '● nodes online · multiplexed over 1 socket</text>' % (ly + 11,))
    a('</svg>')
    return "".join(parts)


def main():
    total, weeks = fetch_weeks()
    svg = build_svg(total, weeks)
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote %s (%d bytes, %d weeks, %d contributions)"
          % (OUT, len(svg), len(weeks), total))


if __name__ == "__main__":
    main()
