# Building a Team of Free Agents

This is an attempt to build a competitive baseball team using only free agents. The inspiration for this is partly inspired by ["2015 All-Star Game Rosters if determined by fWAR"](https://www.reddit.com/r/baseball/comments/34xw91/2015_allstar_game_rosters_if_determined_by_fwar/) posted by /u/rjaspa and partly inspired by ["FanGraphs Crowd: The Top 82 Free Agents"](http://www.fangraphs.com/blogs/fangraphs-crowd-the-top-82-free-agents/).

Some notes on my analysis: "Expected Salary" comes from the Fangraphs Crowd article spreadsheet. For "Expected 2016 fWAR", I used a combination of 2015 and 2014 fWAR with 2015 performance carrying a little more weight. To simplify the analysis, I'm not moving players around the field. Meaning, if the FanGraphs spreadsheet lists them as a LF/CF, those are the only spots I would put them - not RF, for example. I am not selecting a DH for this team, because their true value would be less compared to their listed fWAR since they would not be playing defense (unless I selected someone who was a DH last year). Also "Fuck The DH".

The positions of the 82 free agents listed in the FanGraphs article are distributed like this:

| Position                        | # Players                       | Total Exp. fWAR                 |
|---------------------------------|---------------------------------|---------------------------------|
| LF                              | 18                              | 30.033333334                    |
| C                               | 5                               | 5.066666666                     |
| DH                              | 2                               | 1.033333333                     |
| SS                              | 4                               | 6.6                             |
| CF                              | 7                               | 11.900000001                    |
| P                               | 41                              | 68.366666666                    |
| RF                              | 9                               | 12.9                            |
| 1B                              | 5                               | 9.233333333                     |
| 2B                              | 6                               | 10.366666667                    |
| 3B                              | 3                               | 7.133333334                     |


If we were to just select the player with the highest expected fWAR for each position, you would end up with the team below. For the purposes of this exercise, I am selecting five pitchers to make up the starting rotation:

| Positions               | Player                  | Exp. 2016 fWAR          | Exp. Salary             |
|-------------------------|-------------------------|-------------------------|-------------------------|
| CF                      | Dexter Fowler           | 2.6                     | 13.78009259             |
| LF                      | Yoenis Cespedes         | 5.566666667             | 21.50456621             |
| RF                      | Jason Heyward           | 5.733333333             | 22.71539961             |
| 1B                      | Chris Davis             | 4                       | 20.51440922             |
| 2B                      | Ben Zobrist             | 3.233333333             | 14.14712154             |
| 3B                      | Daniel Murphy           | 2.5                     | 12.6036961              |
| SS                      | Ian Desmond             | 2.466666667             | 14.4125                 |
| C                       | Chris Iannetta          | 1.333333333             | 7.209476309             |
| P                       | David Price             | 6.3                     | 27.54347826             |
| P                       | Zack Greinke            | 5.4                     | 26.71084337             |
| P                       | Johnny Cueto            | 4.266666667             | 21.01016949             |
| P                       | Jordan Zimmermann       | 3.766666667             | 20.79234973             |
| P                       | John Lackey             | 3.2                     | 14.87323944             |
| *Total*                 |                         | *50.366666667*          | *237.817341869*         |


That's great and all, but $238 million in payroll is just a little bit steep. What if instead of just choosing the players with the highest expected fWAR, we chose the players with the highest expected fWAR per dollar they cost?

| Positions          | Player             | Exp. 2016 fWAR     | Exp. Salary        | Exp. Wins/$        |
|--------------------|--------------------|--------------------|--------------------|--------------------|
| CF                 | Rajai Davis        | 1.666666667        | 5.886792453        | 0.283119658        |
| LF                 | Steve Pearce       | 1.833333333        | 7.058510638        | 0.259733735        |
| RF                 | Jason Heyward      | 5.733333333        | 22.71539961        | 0.252398524        |
| 1B                 | Chris Davis        | 4                  | 20.51440922        | 0.194984899        |
| 2B                 | Ben Zobrist        | 3.233333333        | 14.14712154        | 0.228550615        |
| 3B                 | Juan Uribe         | 2.466666667        | 7.794776119        | 0.316451253        |
| SS                 | Asdrubal Cabrera   | 2.033333333        | 9.561983471        | 0.212647652        |
| C                  | Chris Iannetta     | 1.333333333        | 7.209476309        | 0.184941773        |
| P                  | Joe Blanton        | 1.1                | 3.72               | 0.295698925        |
| P                  | Bartolo Colon      | 2.6                | 9.799180328        | 0.265328315        |
| P                  | J.A. Happ          | 2.533333333        | 11.01570681        | 0.229974651        |
| P                  | David Price        | 6.3                | 27.54347826        | 0.228729282        |
| P                  | Mark Buehrle       | 2.433333333        | 10.816             | 0.224975345        |
| *Total*            |                    | *37.266666665*     | *157.782834758*    | *0.236189612908*   |

Okay, $157 million is still pretty steep for a team with no bench and no bullpen. That being said, this team looks like it could win a lot of games while being $80 million less than the previous team.

Anyways, that's all I have the energy for. Possible improvements to this analysis would be:

1. Modify the Expected 2016 fWAR to be based on a projection system such as Steamer.
2. Update the position listings to be more flexible. For instance, let LF/CF players play in RF.
3. Add a DH. We will need to remove the player's defensive WAR for that analysis.
4. Modify it so we can put a "hard cap" on the budget. I want to see what the best $100 million dollar FA team looks like.

You can find the data and code used for this analysis on my [GitHub](https://github.com/ktarrant/freeAgents): 