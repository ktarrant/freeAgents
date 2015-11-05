# Analyzing Baseball Free Agent Class

This is an attempt to build a competitive baseball team using only free agents. The inspiration for this is partly inspired by ["2015 All-Star Game Rosters if determined by fWAR"](https://www.reddit.com/r/baseball/comments/34xw91/2015_allstar_game_rosters_if_determined_by_fwar/) /u/rjaspa and partly inspired by ["FanGraphs Crowd: The Top 82 Free Agents"](http://www.fangraphs.com/blogs/fangraphs-crowd-the-top-82-free-agents/).

Some notes on my analysis: "Expected Salary" comes from the Fangraphs Crowd article spreadsheet. For "Expected 2016 fWAR", I used a combination of 2015 and 2014 fWAR with 2015 performance carrying a little more weight. To simplify the analysis, I'm going to assume that CF will be staying in CF, LF/RF will be staying in their fields, etc. The one exception to that is that I'm letting anyone be a DH.

The positions available in the 2016 FA class looks like this:

| Position                 | # Players                | Total Exp. fWAR          |
|--------------------------|--------------------------|--------------------------|
| LF                       | 18                       | 30.033333334             |
| C                        | 5                        | 5.066666666              |
| DH                       | 2                        | 1.033333333              |
| SS                       | 4                        | 6.6                      |
| CF                       | 7                        | 11.900000001             |
| P                        | 41                       | 68.366666666             |
| RF                       | 9                        | 12.9                     |
| 1B                       | 5                        | 9.233333333              |
| 2B                       | 6                        | 10.366666667             |
| 3B                       | 3                        | 7.133333334              |


If we were to just select the player with the highest expected fWAR for each position:

| Positions          | Player             | Exp. 2016 fWAR     | Exp. Salary        |
|--------------------|--------------------|--------------------|--------------------|
| CF                 | Dexter Fowler      | 2.6                | 13.78009259        |
| LF                 | Yoenis Cespedes    | 5.566666667        | 21.50456621        |
| RF                 | Jason Heyward      | 5.733333333        | 22.71539961        |
| 1B                 | Chris Davis        | 4                  | 20.51440922        |
| 2B                 | Ben Zobrist        | 3.233333333        | 14.14712154        |
| 3B                 | Daniel Murphy      | 2.5                | 12.6036961         |
| SS                 | Ian Desmond        | 2.466666667        | 14.4125            |
| C                  | Chris Iannetta     | 1.333333333        | 7.209476309        |
| P                  | David Price        | 6.3                | 27.54347826        |
| P                  | Zack Greinke       | 5.4                | 26.71084337        |
| P                  | Johnny Cueto       | 4.266666667        | 21.01016949        |
| DH                 | Alex Gordon        | 4.066666667        | 18.64              |
|--------------------|--------------------|--------------------|--------------------|
| Total              |                    | 47.466666667       | 220.791752699      |

