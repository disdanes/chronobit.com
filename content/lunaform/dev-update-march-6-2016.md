Title: Dev Update : Difficulty and World Selection
Slug: lunaform/dev-update-march-6-2016
Date: 2016-03-06 11:00
Authors: Justin Lindsey
Summary: I've been working on easing the difficulty curve and the ability to select different level groups with world selection
Template: lunaform_article
header_cover: /theme/images/lunaform/world_select.jpg

## The difficulty of difficulty

This week I was working on revisiting our first 10 levels and trying to create a much smoother difficulty curve. My goal is to slowly ramp the player into needing better timing and reflexes, but in a way that makes them feel good rather than feeling punished. The unfortunate consequence of having played your own game for so long, is that the developer becomes a bad gauge for how difficult a level is. I tried to make the first 5 levels a tutorial in learning the game concepts. Then the next 5 levels introduce the *Nova Star*, which heals or hurts in an area radius on the hex grid. The Nova Star used to have a timer which would countdown to provide the player some time to deal with it, but I found the timer was not always easily visible. The timer became even more difficult to keep track of when there was more than one Nova Star on the screen. I took out the timer aspect completely, and added a circle underneath the Nova star to indicate the radius it will affect.

![Nova Star](/theme/images/lunaform/novastar.gif)

In rebuilding levels 9 and 10 I became way too focused on the Nova Stars, and the challenge became far too difficult as a result. I used a pattern of blue/orange/blue to try and introduce a situation where you couldn't swap in between each Nova Star, and so you had to observe the first and last stars to know which hexes would be filled at the end of the chain. 

![Too many Nova Stars](/theme/images/lunaform/too_many_novastars.jpg)

The problem with this, is that if the player does not immiediately recognize that chain, it feels very punishing as some hexes will be lost when hit twice by Nova Stars. When I had Molly sit down and do a test run of the new levels, she was extremely frustrated with level 9 and 10. I knew I had to tweak some knobs in order to balance the feeling of being punished vs the level being difficult. At this point in the game I didn't want an incredibly difficult level, just an appropriate challenge for someone who has made it past a couple early levels and the tutorial. Looking at the Nova Stars I've got the following knobs I can tweak:

* Speed of Nova Stars
* Radius of their effect
* Number of Nova Stars spawned
* Sequence of Nova Stars (blue, orange, blue, etc)
* Time between their spawns

Molly made a great point when we were discussing why the level felt so hopeless, and it was due to how hard the Nova Stars hit (they hit for 3, which fills up a neutral hex, or destroys a partially damaged hex) in conjunction with how many there were to deal with. Area effects are powerful enough on their own, that she mentioned how I should be using them much more sparingly than I am. I took her advice and choose to tweak the time between their spawns to the player breathing room between each Nova Star, and hopefully enough time to swap before the next one hits. After updating the levels and getting Molly to try them again, she commented that they were much more enjoyable with the breathing room. I'll definitely need the perspective of some new players to understand if it's still too difficult, or if it starts to feel appropriately challenging, but I don't want players to quit because a level felt 'bad'. It's a difficult balance to strike between a challenge that makes you want to play more, vs a challenge that makes you want to quit and never try again. 

## World Selection

Another aspect that I worked on this week was implementing a way to select each set of levels through a global 'World Selection'. At the moment any planet can be choosen, but eventually I'll add in progression so that you'll need to complete earlier planets before visiting the more difficult ones.

![World Select](/theme/images/lunaform/world_select.gif)

## Dev Notes

For anyone curious, I'm using the [Mad Level Manager](https://www.assetstore.unity3d.com/en/#!/content/10070) to help with the world select and level selection. I've built out level selection in a couple different ways previously, but all of those left lots of features to be desired. For a more complex or ambitious project I'd opt to build out my own level tools over using a third party package, but I think for the scope of Lunaform, Mad Level Manager seems to cover the right feature basis.

Not sure how helpful this is to others, but I created a coroutine for my Nova Star so that it'll wait until it's explosion animation clip is played before it executes the rest of the effect. Callback in this case is a C# delegate, which I'm just borrowing from the excellent [Messenger + Callback](http://wiki.unity3d.com/index.php?title=Advanced_CSharp_Messenger) code from the unity wiki. My use case is fairly simple and assumes only a single animation layer, for more complex cases this will need to be expanded on to be more generic. 

	:::csharp
    IEnumerator WaitForCurrentClipLength(Callback callback){
        // Will wait for the exact animation time
        // Only if the animation is definitely playing during this time
        yield return new WaitForEndOfFrame();
        yield return new WaitForSeconds(anim.GetCurrentAnimatorStateInfo(0).length);
        callback();
    }

    void setupExplode()
    {
        anim.SetTrigger(explodeAnimHash);
        StartCoroutine(WaitForCurrentClipLength(Explode));
    }
    
    void Explode(){
    	// All my explosion effects
    	// Casts an overlap circle, enumerates colliders
    	// Performs specific on collision action
    }
    



