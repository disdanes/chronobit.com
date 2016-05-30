Title: Dev Update : Upgrades!
Slug: lunaform/upgrades-update-march-28-2016
Date: 2016-03-28 12:00
Authors: Justin Lindsey
Summary: Lunaform has a couple of upgrades to give the player something to work towards, and to help balance out some of the more challenging levels. I've been working on improving how the player earns the upgrades, and how the player uses the upgrades.
Template: lunaform_article
header_cover: /theme/images/lunaform/upgrades_cover.jpg

## How about some upgrades with those upgrades

I've been working on the upgrades in Lunaform to address some of the early player feedback we got. Many people didn't know there were upgrades in the game. We used a poor mechanism to communicate how you earned upgrades, and it wasn't obvious that upgrades were available. The easy to ignore bar at the bottom of the screen would fill up with each successful collision, and when you reached 50 you could click on HUGO to enter the upgrade menu.

![Old Upgrades](/theme/images/lunaform/old_upgrades.jpg)

I can't blame anyone for not clicking on HUGO (the robot) in the corner. He doesn't exactly look clickable, and there is zero intuition for clicking a character to trigger a menu for buying upgrades. It doesn't help that the upgrade menu is sitting in the corner competing for actions within the main gameplay loop. A player would have to actively *stop* playing the game to acknowledge HUGO. Within that interruption they have to figure out what the upgrades do, how to buy them, use them, and whether or not they even help.

![Old Upgrade Menu](/theme/images/lunaform/old_upgrade_menu.jpg)

These upgrades (shield, turret, bomb) lost some of that anticipation because the user just 'got' the upgrade without any instructions on how to use them. The shield could absorb hits from opposite stars, but the player could only find that out if they 'double clicked' on a hex to apply the shield. The bomb would blow up and fill hexes, but only if it was allowed to 'tick' up. The turret could change the colors of the stars, but only if it was configured to shoot in a certain direction. Each upgrade took some work to use, but that divided the player's attention away from the action. 

It's kind of like asking the player to stop mid-combat in Diablo to evaluate their gear and determine what they should be wearing. There is a reason why people like to pour over loot while in the safe confines of the town. It gives them a breather from the action, lets their mind focus on a different aspect of the game, and builds anticipation for the next encounter as an opportunity to use the upgrades. 

## Upgrades 1.5

### Where to get upgrades ?

I think many games have their upgrades outside of the main gameplay loop in order to provide a breather, and build anticipation for the next level. Placing the upgrade menu in the level select will allow a place to go between the levels for a nice break. There is a good stopping point after the first tutorial world where the player can earn the 'Upgrade Store'. The player will have seen some of the game and gameplay, and can start to reason about what upgrades might be worth working towards. Here's a *concept* example of the new upgrade store:

![Upgrade Store](/theme/images/lunaform/new_upgrade_menu.jpg)

### Something to work towards

There should be a way to earn upgrades that promotes playing the game and mastering the level challenges. Earning 'energy' for filling a hex up is a nice short term goal, but becomes problematic when it doesn't always promote 'playing' the game. The stars spawn constantly, and a keen eyed player would be tempted to let the game idle until they had enough energy to buy all the upgrades. In order to promote playing the level and filling up all of the hexes, we want to reward the player proportionally to how well they beat the level. The way you beat a level of Lunaform is to fill up all the hexes by swapping them so they collide with the stars of the same color. The way you lose a level of Lunaform is by having all the hexes get destroyed by them colliding with stars of a different color. In the new upgrade system, the player will be rewarded by how many full hexes survived at the end of the level. The player will earn a 'hex' for each full hex that survived, and then they can use the 'hexes' to purchase upgrades at the upgrade store. The maximum a player can earn for each level is directly equal to the number of 'hexes' in that level, and hopefully promotes replaying the level if the player was unable to get all the 'hexes' on the first try. Here's an example of the updated rewards screen:

![Victory Screen](/theme/images/lunaform/victory_screen.gif)

### How to use the upgrades ?

Previously, upgrades would just be 'applied' to your game state in Lunaform. Upgrading any of the categories (shield, turret, bomb) would cause an existing 'hex' to turn into an upgraded one. I wanted to move away from auto-applying the upgrades and into a system where the player could interact *more* with the game through the upgrades. Many of the upgrades are still a work in progress, but I'm excited for the 'Time Stop' upgrade. At one point a player had discovered they could still swap hexes while the game was paused, and started trying to exploit it to beat some of the really challenging levels! I really loved what that player had discovered, so I decided to formalize that into an upgrade. Here's an early preview of Time Stop:

![Time Stop](/theme/images/lunaform/timeStopPreview.gif)

The concept of Time Stop is to allow you to swap hexes without having any of the stars move. It lets you line up the colors, and gives you some time to anticipate where the stars are headed. With this new skill, I wanted to create a better way of using it so I created a skill bar. I'm still evaluating if the skill bar is the best mechanism for using skills in Lunaform, but it allows the player to periodically invoke an upgrade and know when the upgrade is ready to use again.

## Upcoming Build Update

The current demo build is getting out of date on the site, which is good news! There have been quite a few improvements to Lunaform, and I'm excited to share it with everyone and get some thoughts and feedback on the changes. In the next two weeks I'm going to be sending out an updated build to folks who are interested in play testing and giving me feedback. If your interested in playtesting, and want to help me make Lunaform even better, just subscribe to Lunaform updates in the footer below!



