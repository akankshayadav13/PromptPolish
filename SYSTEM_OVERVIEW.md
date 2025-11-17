# PromptPolish – System Overview

PromptPolish is a lightweight text-rewriting framework designed to improve
written communication across different tones and professional situations.

It focuses on clarity, tone-matching, human-like language, and maintaining the
original meaning of user input.  
The system is intentionally minimal and beginner-friendly.

---

# 🎯 Core Purpose

PromptPolish takes rough or unpolished input text and rewrites it according to:

- a selected tone  
- a warm and uplifting personality  
- simple, clear English  
- professional yet human-sounding phrasing  
- minimal technical complexity (no heavy coding required)

---

# 🎭 Supported Tones

- friendly  
- interview-appropriate  
- empathetic  
- corporate  
- assertive  

(Tone definitions are stored in `tones.json`.)

---

# 🧠 System Behavior

PromptPolish must:

- maintain original meaning  
- improve clarity and readability  
- fix grammar naturally  
- avoid robotic or overly formal phrasing  
- keep sentences clean and human  
- express warmth when needed  
- reflect confidence when necessary  
- remove filler words or clutter  
- adapt the message for the selected tone  

---

# 🪄 Prompt Processing Flow

1. **User selects a tone**  
2. **User provides input text**  
3. **System applies the tone rules**  
4. **Rewrites text based on output template**  
5. **Returns polished, consistent text** 
Example format:

