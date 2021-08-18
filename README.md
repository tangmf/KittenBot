# KittenBot
![Kitten](/Images/meow.png)


KittenBot is a very simple discord bot, and acts as a pet that will require it to be taken care of. There are 3 main stats that users will need to monitor; health, hunger and happiness. As time goes on, these stats will slowly drop, and it is up to members of the server to feed, play and care for it.

![Profile](/Images/screenshot.png)

## How the stats change over time
* Every minute, hunger and happiness decrease by 5 and 2 respectively.
* Once the hunger reaches 0, the next time the stats decrease, health will be decreased by 5.

## Commands
* help: Shows all commands for the bot.
* ping: Pings the bot, where the bot will reply with the response time in ms.
* feed: Feeds the bot, increasing its hunger by 10 and happiness by 2.
* snuggle: Makes the bot snuggly and warm, increasing its happiness by 10.
* status: Shows the values of the stats; health, hunger, happiness
* sleep: Lets the bot sleep, where it will gain 5 happiness and 10 health. Sets the bot to idle.
* wakeup: Wakes up the bot, where it will gain 5 health. Sets the bot back to online.
* rename: Rename the bot, where in .rename <new name>, replace <new name> with the bot's new name.
  

