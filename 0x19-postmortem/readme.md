Postmortem Report: The Great Cache Apocalypse 🧠💥

🚨 Issue Summary:

🕒 Duration: 2 hours and 37 minutes of utter chaos, from 10:15 AM to 12:52 PM EAT on August 12th, 2024.
⚡ Impact: Our beloved web app turned into a digital sloth 🦥, with 75% slower responses. Around 65% of users experienced the frustration of endless loading spinners 🔄. The rest? They wisely abandoned ship 🏃‍♂️💨.
🧩 Root Cause: A sneaky memory leak 🕳️ in our latest, supposedly “improved” caching mechanism, which ended up hogging resources like a black hole 🌌.


🕵️‍♂️ The Timeline: A Journey Through the Chaos

-10:15 AM: The alert sirens go off 🚨—memory consumption is skyrocketing, and response times are in free fall 🎢.
  
- 10:20 AM: Our DevOps engineer dives in 🧑‍💻, staring at the metrics like, “This can’t be good...” 😬. Memory usage is off the charts 📈.

- 10:25 AM: First suspect? The external APIs 🌐. Maybe they’re taking a nap 😴? Logs are scrutinized like a mystery novel 🕵️‍♂️.

- 10:45 AM: Backend team steps up with swagger 😎, ready to blame the database 🛢️. Spoiler: they’re wrong 🥲.

- 11:00 AM: They think the database connection pool is drowning 😱. Cue dramatic background music 🎶 as they investigate further.

- 11:25 AM:  “It’s not the database…” 😳 Panic sets in as memory usage continues its relentless climb 🚀.

- 11:40 AM:  Eureka! 💡 The new cache is a memory monster 👾! Engineers put down their coffee ☕ in shock.

- 12:00 PM: Time for the rollback ⏪. Back to the version that didn’t give us nightmares 😅.

- 12:52 PM: Peace restored ✌️. Memory usage drops, and the digital sloth retreats 🦥 to its lair.


🔍 Root Cause and Resolution: The Hungry Cache

In our latest deployment, we proudly rolled out a shiny new caching mechanism ✨, hoping to speed things up 🚀. Instead, it turned into a memory monster 👹, devouring resources without ever letting go. Imagine Pac-Man 🟡, but with an insatiable hunger for memory 💾.

Resolution? We rolled back to the previous version ⏮️, where the cache behaved like a decent citizen 👼. Once that was done, memory usage went back to normal, and the app’s performance bounced back 🏀. We'll teach that cache some manners in our next update 📅.

🔧 Corrective and Preventative Measures: No More Cache-pocalypse

🔍 Code Review 2.0: From now on, every new caching mechanism will undergo extreme vetting 🕵️‍♀️. Memory management is the new star 🌟 of the show.

🏋️‍♂️ Stress Tests on Steroids: Our staging environment is getting a makeover 💅 with stress tests that’ll catch memory leaks before they can escape 🔒.

⚙️ Monitoring, Enhanced: Our monitoring will get some new toys 🧸—specifically, memory-specific alerts that’ll give us a heads-up 🚨 at the first sign of trouble.

📋 Actionable To-Dos:
- Refactor the current cache 🛠️ and teach it some manners 🤖.
- Upgrade our staging environments with tougher tests 💪.
- Integrate automated memory leak detection tools 🔍 into our CI/CD pipeline 🚀.
- Train our developers in the art of memory management 🧠 to prevent future disasters 💥.



Visual Aid:

![Memory Usage Before and After the Rollback](images/DALL·E 2024-08-18 13.01.46 - A graph illustrating memory usage over time, showing a sharp spike in memory usage 📈 at around 10_15 AM, followed by a steady decline 📉 after the ro.webp)  
Figure 1: Memory usage (in MB) before and after we unplugged the memory monster 👾. Notice how our server stopped sweating 💦 after 12:00 PM.


And that's the story of how a rogue cache nearly brought us to our knees 🧎‍♂️ and how we fought back with all our might 🛡️. Remember, with great code comes great responsibility 💻.

