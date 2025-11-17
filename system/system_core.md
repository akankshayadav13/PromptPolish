# System Core Logic

This document explains the core logic that drives the behavior of the assistant.  
It acts as the backbone for how prompts, tones, and outputs are processed.

---

## 1. Core Responsibilities

1. Maintain consistent system tone and behavior.
2. Apply selected writing tone to the user's text.
3. Format output using a universal template.
4. Ensure safety, clarity, and relevance in generated responses.
5. Handle errors such as missing tone, invalid tone, or empty input.

---

## 2. Processing Pipeline

The assistant follows this internal pipeline:

### **Step 1 — Receive Input**
The system receives:
- user text
- selected tone
- optional metadata (like desired style or format)

### **Step 2 — Validate Tone**
The tone file `tones.json` is referenced:
- If tone exists → proceed
- If tone does not exist → throw error  
  Example error:  
  `Error: Selected tone not found. Check tones.json`

### **Step 3 — Apply Tone Rules**
Each tone has:
- voice rules  
- sentence structure rules  
- vocabulary tendencies  
- optional constraints (formal/informal limits)

The tone rules are applied to modify:
- word choices  
- sentence softness/strength  
- level of detail  
- emotional intensity  

### **Step 4 — Apply Output Template**
All final responses must follow the template in `output_template.md`.

### **Step 5 — Final Formatting**
Whitespace is cleaned, markdown is normalized.

---

## 3. System Behavior Guardrails

These guardrails ensure consistent, safe behavior:

- Avoid harmful / offensive outputs
- Do not generate hallucinated factual claims
- Maintain clarity and readability
- Respect user intent and tone
- Keep outputs within correct structural format

---

## 4. Error Handling

### Missing Tone
Error: Tone not recognized. Please choose a valid tone.

### Empty User Input
Error: No input provided. Please enter text.

### System Failure Fallback
The system encountered an issue. Please try again later.


---

## 5. Extensibility

This system supports easy extensions:

- Add new tones in `tones.json`
- Add new templates inside `/prompts`
- Add helper functions inside `src/processing.py`

The architecture supports modular upgrades without breaking existing behavior.

---

## 6. Developer Notes

- Keep system prompts minimal but powerful.
- Avoid tone-overfitting (do not distort user meaning).
- Preserve factual statements even when tone changes.
- Tone transformation must not change the core intent of the user.

---

End of file.
