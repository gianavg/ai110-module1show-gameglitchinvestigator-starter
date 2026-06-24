# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
When i first played a game , told me to go lower and higher, once the game ended my guess was much higher and the actual answer was in the negatives, so not between 1-100.The second time when i used thre hint button , it displayed no hint and seemed unresponsive.The easy diificultly setting dosnt display the correct range either.

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|  100  |   too high        |    no response  |    none                |     
|  90   |   too high        |    go higher    |    none                |       
|  50   |   too low         |    go lower     |    none                |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
i used copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The ai suggested changing the hint to correctly depend on the same numeric type for both the guess and secret, i had the ai run both its own test and i tested it as well
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I had the ai run a test case and then tested the app myslef with seprate test cases after each major fix
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I tested to make sure the code would recognize that 1 is the lowest value, and that the hint should only ever be go higher or winner but never go lower.the fact it kept saying go lower showed be it wasnt a logic issue but an issue with how data types were being handld

- Did AI help you design or understand any tests? How?
I explained certain logic within the orginal code to me so i correctly understood what i was missing or what needed to be fixed.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
