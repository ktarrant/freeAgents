# Building a Team of Free Agents

This is an attempt to build a competitive baseball team using only free agents. The inspiration for this is partly inspired by ["2015 All-Star Game Rosters if determined by fWAR"](https://www.reddit.com/r/baseball/comments/34xw91/2015_allstar_game_rosters_if_determined_by_fwar/) posted by /u/rjaspa and partly inspired by ["FanGraphs Crowd: The Top 82 Free Agents"](http://www.fangraphs.com/blogs/fangraphs-crowd-the-top-82-free-agents/).

Some notes on my analysis: "Expected Salary" comes from the Fangraphs Crowd article spreadsheet. For "Expected 2016 fWAR", I used the current Steamer projected fWAR value for the player. To simplify the analysis, I'm not moving players around the field. Meaning, if the FanGraphs spreadsheet lists them as a LF/CF, those are the only spots I would put them - not RF, for example. I am not selecting a DH for this team, because their true value would be less compared to their listed fWAR since they would not be playing defense (unless I selected someone who was a DH last year). Also "Fuck The DH".

The positions of the 82 free agents listed in the FanGraphs article are distributed like this:

| Position                        | # Players                       | Total Exp. fWAR                 |
|---------------------------------|---------------------------------|---------------------------------|
| LF                              | 18                              | 20.5                            |
| C                               | 5                               | 6.7                             |
| DH                              | 2                               | 0.6                             |
| SS                              | 4                               | 5.0                             |
| CF                              | 7                               | 7.5                             |
| P                               | 41                              | 62.1                            |
| RF                              | 9                               | 8.6                             |
| 1B                              | 5                               | 6.8                             |
| 2B                              | 6                               | 8.2                             |
| 3B                              | 3                               | 4.8                             |


If we were to just select the player with the highest expected fWAR for each position, you would end up with the team below. For the purposes of this exercise, I am selecting five pitchers to make up the starting rotation:

| Positions               | Player                  | Exp. 2016 fWAR          | Exp. Salary             |
|-------------------------|-------------------------|-------------------------|-------------------------|
| P                       | David Price             | 5.3                     | 27.54347826             |
| P                       | Zack Greinke            | 4                       | 26.71084337             |
| P                       | Hisashi Iwakuma         | 3.7                     | 14.48186528             |
| P                       | Johnny Cueto            | 3                       | 21.01016949             |
| P                       | Jaime Garcia            | 2.9                     | 13.25988701             |
| C                       | Matt Wieters            | 2.2                     | 12.64895636             |
| CF                      | Denard Span             | 2.2                     | 11.96629213             |
| LF                      | Alex Gordon             | 3.5                     | 18.64                   |
| RF                      | Jason Heyward           | 4.7                     | 22.71539961             |
| 1B                      | Chris Davis             | 2.4                     | 20.51440922             |
| 2B                      | Ben Zobrist             | 3.1                     | 14.14712154             |
| 3B                      | Daniel Murphy           | 2.1                     | 12.6036961              |
| SS                      | Ian Desmond             | 1.6                     | 14.4125                 |
| *Total*                 |                         | *40.7*                  | *230.65461837*          |

According to [this link](http://www.fangraphs.com/library/misc/war/replacement-level/), a team of replacement level players should accumulate about 47.4 wins over a full season. Let's assume you made a team by signing all these players and then filling out your bullpen and bench with replacement level players. We would expect this team to win about 88.1 games. That's great and all, but $238 million in payroll is just a little bit steep. What if instead of just choosing the players with the highest expected fWAR, we chose the players with the highest expected fWAR per dollar they cost?

| Positions          | Player             | Exp. 2016 fWAR     | Exp. Salary        | Exp. Wins/$        |
|--------------------|--------------------|--------------------|--------------------|--------------------|
| P                  | Bud Norris         | 1.9                | 6.388888889        | 0.297391304        |
| P                  | Hisashi Iwakuma    | 3.7                | 14.48186528        | 0.25549195         |
| P                  | Rich Hill          | 1.5                | 6.523809524        | 0.229927007        |
| P                  | Jaime Garcia       | 2.9                | 13.25988701        | 0.218704729        |
| P                  | Bartolo Colon      | 2.1                | 9.799180328        | 0.214303639        |
| C                  | Chris Iannetta     | 1.5                | 7.209476309        | 0.208059495        |
| CF                 | Denard Span        | 2.2                | 11.96629213        | 0.183849765        |
| LF                 | Ben Zobrist        | 3.1                | 14.14712154        | 0.219125848        |
| RF                 | Jason Heyward      | 4.7                | 22.71539961        | 0.206908092        |
| 1B                 | Steve Pearce       | 1.2                | 7.058510638        | 0.170007536        |
| 2B                 | Howie Kendrick     | 2.4                | 13.22995781        | 0.181406474        |
| 3B                 | Juan Uribe         | 1.5                | 7.794776119        | 0.192436573        |
| SS                 | Jimmy Rollins      | 1.3                | 7.432653061        | 0.174903899        |
| *Total*            |                    | *30.0*             | *142.007818248*    | *0.211255974285*   |

Howie Kendrick, Juan Uribe, Jimmy Rollins... is this the Dodgers? $142 million is still pretty steep for a team with no bench and no bullpen. But it's $90 million less than the previous team with only 10 less wins. If we did the same as above, where we filled out the bench and bullpen with replacement level players, we would expect this team to win about 77.6 games. 

Anyways, that's all I have the energy for. Possible improvements to this analysis would be:

1. Update the position listings to be more flexible. For instance, let LF/CF players play in RF. A downside with this is that fWAR is position-adjusted, so we will probably lose accuracy by moving players around.
2. Add a DH. We will need to remove the player's defensive WAR for that analysis.
3. Modify it so we can put a "hard cap" on the budget. I want to see what the best $100 million dollar FA team looks like.

You can find the data and code used for this analysis on my [GitHub](https://github.com/ktarrant/freeAgents).