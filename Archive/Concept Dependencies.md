# Concept Dependencies

This document maps how the teaching concepts in Rolling Rocks Downhill build upon each other.

---

## Visual Dependency Map

```
┌─────────────────────────────────────────────────────────────────┐
│                    FOUNDATIONAL CONCEPTS                        │
│                                                                 │
│  ┌─────────────────────────────┐    ┌───────────────────────┐  │
│  │ Quality-Speed Trade-off    │    │  Evaporating Cloud    │  │
│  │ (False Assumption)         │    │  (Thinking Tool)      │  │
│  │ Ch 3, 7, 34                │    │  Ch 13-14             │  │
│  └─────────────┬───────────────┘    └───────────────────────┘  │
└────────────────┼───────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                     QUALITY CONCEPTS                            │
│                                                                 │
│  ┌─────────────────────────────┐                               │
│  │   Dog Food Problem          │                               │
│  │   Ch 16-17                  │                               │
│  └─────────────┬───────────────┘                               │
│                │                                                │
│                ▼                                                │
│  ┌─────────────────────────────┐                               │
│  │ Late vs. In-Process         │                               │
│  │ Inspection                  │                               │
│  │ Ch 17                       │                               │
│  └─────────────┬───────────────┘                               │
└────────────────┼───────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                      FLOW CONCEPTS                              │
│                                                                 │
│  ┌─────────────────────────────┐                               │
│  │   Small Batches             │                               │
│  │   Ch 25-26                  │                               │
│  └─────────────┬───────────────┘                               │
│                │                                                │
│                ▼                                                │
│  ┌─────────────────────────────┐                               │
│  │   French Fry Revelation     │                               │
│  │   (Replenish on Demand)     │                               │
│  │   Ch 26                     │                               │
│  └─────────────┬───────────────┘                               │
└────────────────┼───────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                     THE SYNTHESIS                               │
│                                                                 │
│  ┌─────────────────────────────┐                               │
│  │     INVERTED PYRAMID        │◀── Steve's own discovery     │
│  │     Ch 33-34                │    (from "Made to Stick")    │
│  └─────────────┬───────────────┘                               │
│                │                                                │
│                ▼                                                │
│  ┌─────────────────────────────┐                               │
│  │   "Good Enough to Ship"     │                               │
│  │   Ch 34                     │                               │
│  └─────────────────────────────┘                               │
└─────────────────────────────────────────────────────────────────┘
```

---

## The Eight Core Concepts

### 1. [[Quality Speed Tradeoff|Quality-Speed Trade-off]] (False Assumption)
- **Builds on:** Nothing - this is the conventional wisdom to be challenged
- **What builds on it:** Everything else challenges this assumption
- **Key quote:** "Our current strategy is to deliver sooner by lowering quality."

### 2. [[Evaporating Cloud|Evaporating Cloud]]
- **Builds on:** Nothing - this is Craig's foundational thinking tool
- **What builds on it:** Steve's ability to analyze conflicts (and his career decision in Ch 60)
- **Key quote:** "Whenever I want to solve a significant problem, I describe it using this diagram called an evaporating cloud."

### 3. [[Dog Food Problem|Dog Food Problem]]
- **Builds on:** [[Quality Speed Tradeoff|Quality-Speed Trade-off]] (challenges it)
- **What builds on it:** [[Late vs In Process Inspection|Late vs. In-Process Inspection]]
- **Key quote:** "No one ever tasted it before serving it... frankly—we didn't care."

### 4. [[Late vs In Process Inspection|Late vs. In-Process Inspection]]
- **Builds on:** [[Dog Food Problem|Dog Food Problem]]
- **What builds on it:** [[Small Batches|Small Batches]]
- **Key quote:** "You moved from late inspections—testing or tasting at the end of the process when it's very expensive to fix stuff—to in-process inspections, where you build quality into your product during the process."

### 5. [[Small Batches|Small Batches]]
- **Builds on:** [[Late vs In Process Inspection|Late vs. In-Process Inspection]]
- **What builds on it:** [[French Fry Revelation|French Fry Revelation]]
- **Key quote:** "It was like I was an oyster and he'd planted a bit of grit inside my shell, hoping I'd turn it into a pearl."

### 6. [[French Fry Revelation|French Fry Revelation]] (Replenish on Demand)
- **Builds on:** [[Small Batches|Small Batches]]
- **What builds on it:** [[Inverted Pyramid|Inverted Pyramid]]
- **Key quote:** "Our serving staff keeps an eye on how many chips they've got out front, and when it gets too low, they shout out and we cook more."

### 7. [[Inverted Pyramid|Inverted Pyramid]]
- **Builds on:** ALL previous concepts (this is [[Steve Abernethy|Steve's]] synthesis)
- **What builds on it:** [[Good Enough to Ship|Good Enough to Ship]]
- **Key quote:** "I want us to invert FPP by delivering the most important paragraph first, then the next most important paragraph, and so on until we hit December 1st."

### 8. [[Good Enough to Ship|Good Enough to Ship]]
- **Builds on:** [[Inverted Pyramid|Inverted Pyramid]]
- **What builds on it:** The practical implementation of FPP
- **Key quote:** "Good enough to ship. We still won't ship until December 1st, but I want the code and the documentation and everything else for each small chunk fully tested, fully reworked and good enough quality that we could ship it, were it time."

---

## Teaching Sequence

| Order | Concept | Chapter | Teacher |
|-------|---------|---------|---------|
| 1 | [[Quality Speed Tradeoff\|Quality-Speed Trade-off]] | 3, 7, 34 | (Assumed, then challenged) |
| 2 | [[Evaporating Cloud\|Evaporating Cloud]] | 13-14 | [[Craig Lally\|Craig]] |
| 3 | [[Dog Food Problem\|Dog Food Problem]] | 16-17 | [[Cheryl\|Cheryl]] |
| 4 | [[Late vs In Process Inspection\|Late vs. In-Process Inspection]] | 17 | [[Craig Lally\|Craig]]/[[Cheryl\|Cheryl]] |
| 5 | [[Small Batches\|Small Batches]] | 25-26 | [[Craig Lally\|Craig]]/[[Cheryl\|Cheryl]] |
| 6 | [[French Fry Revelation\|French Fry Revelation]] | 26 | [[Cheryl\|Cheryl]] |
| 7 | [[Inverted Pyramid\|Inverted Pyramid]] | 33-34 | [[Steve Abernethy\|Steve]] (self-discovery) |
| 8 | [[Good Enough to Ship\|Good Enough to Ship]] | 34 | [[Steve Abernethy\|Steve]] |

---

## Concept Origins

| Concept | Manufacturing/Kitchen Origin | Software Application |
|---------|------------------------------|---------------------|
| [[Dog Food Problem\|Dog Food]] | Staff eat their own food | Use your own software |
| [[Late vs In Process Inspection\|Late Inspection]] | Taste at end, throw away bad soup | Test at end, expensive rework |
| [[Late vs In Process Inspection\|In-Process Inspection]] | Check ingredients before adding | Test during development |
| [[Small Batches\|Small Batches]] | Cook vegetables in small amounts | Deliver features incrementally |
| [[French Fry Revelation\|Replenish on Demand]] | Cook chips when supply gets low | Build features when needed |
| [[Inverted Pyramid\|Inverted Pyramid]] | Journalism - lead with the lede | Deliver most important first |
| [[Good Enough to Ship\|Good Enough to Ship]] | Each batch could be served | Each increment is releasable |

---

## Key Insight

The dependency map shows that the [[Inverted Pyramid|Inverted Pyramid]] is not just one more concept—it's [[Steve Abernethy|Steve's]] personal synthesis of everything he learned from [[Craig Lally|Craig]] and [[Cheryl|Cheryl]]. This is why Craig plants ideas ("try not to think about small batches") rather than giving answers: Steve needs to discover the synthesis himself.

---

← [[INDEX|Back to Index]] | [[Story Arc|Story Arc]] →
