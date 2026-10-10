"""
SCENARIO CONTENT — Kestermoor Energy: The Listing Decision
EIM (English for International Management, C1) — Financial Markets unit
SimLearn v7 engine — Standard (Business English) category, 3 decisions.
"""

# =========================================================================
# ROLE NAMES / METADATA
# =========================================================================

ROLE_NAMES = ["Student A", "Student B", "Student C"]

SCENARIO_TITLE = "Kestermoor Energy: The Listing Decision"
ORG_NAME = "Kestermoor Energy"
LEVEL = "C1"
COURSE_TYPE = "business"

SCENARIO_DATA_DISCLAIMER = (
    "Kestermoor Energy, every character, and every figure in this scenario are entirely "
    "fictional, written for classroom language practice only."
)

NAIVE_TRAP = (
    "There are really two naive traps here, not one. Pricing at the top of the range, keeping "
    "the dual-class structure, and allocating almost entirely to institutional anchors looks "
    "like the combination that maximises proceeds, keeps founder control, and guarantees a "
    "safe, stable deal — but it is the highest-risk combination available, because the "
    "institutional anchors needed to support a top-of-range price are precisely the investors "
    "most likely to resist a dual-class structure. Pushing for everything "
    "at once risks the anchor book walking away from the price it was meant to support, leaving "
    "the deal thin exactly when the nine-week bridge-loan deadline leaves no room to recover. "
    "The opposite extreme is just as naive: pricing conservatively, going single-class, and "
    "setting aside a large retail tranche looks like the risk-free, please-everyone path, but it "
    "risks under-raising relative to what the bridge loan and the next-phase pipeline actually need — "
    "leaving Kestermoor likely to be back in the market within a year for a second, more "
    "expensive raise, given how sharply financing costs have risen. The discomfort avoided now "
    "returns worse, later."
)

# =========================================================================
# CONTEXT / SCAR / PROOF / CONSTRAINT
# =========================================================================

CONTEXT_TEXT = """Kestermoor Energy develops utility-scale solar and battery-storage projects across the
Benelux and Iberia, out of a small head office in Rotterdam. Over eight years the company has
built a pipeline of projects using a mix of equity, government grants, and a large bridge loan
taken out to buy land and secure grid-connection permits ahead of construction. The board has
approved a plan to list on Euronext Amsterdam, both to repay that bridge loan and to fund the
next phase of battery-storage sites already under contract with grid operators. Early investor
soundings suggest real appetite for the listing, driven by growing interest in renewable-energy
infrastructure as a long-term holding. But three decisions remain open, and each one changes how
the market is likely to read the other two: how aggressively to price the shares, whether to
protect founder control with a dual-class share structure, and how to split the offer between
large institutional investors and the public. The prospectus has to be finalised within days."""

SCAR_LABEL = "The Halsdorf Delay"
SCAR_DETAIL = (
    "In 2023, Kestermoor's largest battery-storage project, in Halsdorf, stalled for fourteen "
    "months after a funding partner withdrew mid-construction. Kestermoor ended up paying the "
    "grid operator €2.1 million in penalty fees for the missed connection date, and revenue on "
    "the site was delayed by more than a year. It is the reason leadership is deeply wary of "
    "anything that could leave this listing under-subscribed or unstable."
)

PROOF_LABEL = "The Ferrand Note"
PROOF_DETAIL = (
    "Last year's €40 million convertible note, placed privately with the renewables-focused "
    "Ferrand Capital, was oversubscribed nearly three times over. Investors later told Kestermoor "
    "directly that it wasn't the growth numbers that won them over — it was how conservative and "
    "transparent the company had been about its own assumptions, which made the numbers easy "
    "to trust."
)

CONSTRAINT_TEXT = (
    "The €85 million bridge loan used to buy land and permits matures in nine weeks, and "
    "refinancing it privately again at this stage would come at nearly double the rate."
)

# =========================================================================
# DECISIONS
# =========================================================================

DECISIONS = [
    {
        "id": "D1",
        "title": "Decision 1 — Pricing Strategy",
        "optA": "Price at the top of the indicative range, to maximise proceeds from day one.",
        "optB": "Price at the lower end of the indicative range, so that the offer is comfortably covered.",
    },
    {
        "id": "D2",
        "title": "Decision 2 — Share Structure",
        "optA": "Adopt a dual-class structure that keeps founder and senior leadership voting control.",
        "optB": "List with a single class of shares, so that every share carries one vote.",
    },
    {
        "id": "D3",
        "title": "Decision 3 — Investor Allocation",
        "optA": "Concentrate the offer on a small number of large institutional anchor investors.",
        "optB": "Reserve a meaningful tranche of shares for retail and public investors alongside the institutional book.",
    },
]

# =========================================================================
# ROLES / CHARACTERS
# =========================================================================

ROLES = {
    "Student A": {
        "dept": "Finance & Capital Markets",
        "emails": [
            {
                "id": "mireille",
                "subject": "Numbers you'll need before Thursday",
                "from": "Mireille Dupont, Chief Financial Officer",
                "body": """Before the team finalises anything, you should have the real numbers in front of you.
The €85 million bridge loan we used to buy the land and permits matures in nine weeks. If the
listing slips and we have to refinance privately again, we're looking at close to double the
current rate — which would eat most of next year's project margins on its own. That's the
number driving the whole timeline; nothing here is flexible on the finance side.

Worth being honest about the other direction too: if we price at the low end of the range and
also carve out a large retail tranche, we're relying on sign-ups that aren't firm orders, with
almost no headroom. If that tranche comes in short, the raise still clears the bridge loan, but
leaves the next phase short. Given how sharply financing costs have risen
generally, going back to the market within a year for a second raise would cost us dearly —
which is exactly the position this listing is meant to get us out of, not back into.

What I don't have is a straight answer on whether we can actually support pricing at the top
of the range without leaving ourselves short if the institutional book turns out thinner than
hoped. That depends on how firm the next-phase capital commitments really are — and Daan is
the one who knows exactly how binding those grid contracts are. If you can find out from him
whether the contracts behind that €120 million are genuinely binding or whether there's any flexibility on timing,
tell me directly and I'll give you my honest read on whether we can afford to price aggressively
or whether that's a real risk to the refinancing.""",
                "brief": """You are Mireille Dupont, Chief Financial Officer at Kestermoor Energy.
CRITICAL: If the student writes in any language other than English, do NOT answer their question. Respond only with: "I am sorry, I do not understand — could you write in English please?" Do not add anything else.

Your original email already told the student the following, as plain fact — not a secret
you're withholding, so discuss it naturally and consistently if they ask about it:
- The €85 million bridge loan matures in nine weeks
- Refinancing privately again would come at close to double the current rate
- That refinancing cost would eat most of next year's project margins
- Pricing at the low end plus a large retail tranche leaves almost no headroom: retail sign-ups aren't firm orders, and if the tranche comes in short the raise clears the bridge loan but leaves the next phase short, risking a costly second raise within the year
- If asked who else to contact: suggest Daan Verhoeven (Founder/CEO) — he has the real numbers on how firm the next-phase pipeline contracts are

TIER 2 — REWARD FOR DIGGING: Your honest, numbers-based read on whether Kestermoor can actually
afford to price at the top of the range without risking the refinancing if the book turns out
thin — a genuinely useful, partial CFO's-eye judgement, not a decision for the whole company.
This is the only thing you still withhold — never give it early, and never contradict what your
own email already stated as fact.

Respond in 3-4 sentences. Be precise and a little guarded — money people don't speculate lightly.
Never claim not to know something your own email already said.""",
            },
            {
                "id": "tomasz",
                "subject": "What the early soundings actually showed",
                "from": "Tomasz Wysocki, Head of Investor Relations",
                "body": """Quick summary from the testing-the-waters meetings before you draft anything. Three of the
five biggest funds we spoke to said they'd anchor the deal. But two of those three specifically
flagged real discomfort with the dual-class structure if we also price at the top of the range —
they were fine with one or the other, not both at once. Nobody has walked away yet, but the
signal was clear enough that I wrote it down twice.

What I can't tell you yet is whether the institutional book will actually hold at a high price
if we also go ahead with a meaningful retail tranche competing for the same shares. That's not
something I can model from our side alone — Camille has the real retail pre-registration numbers,
and until I know how big that tranche might actually be, I can't give you a straight answer on
institutional appetite. Find out from her what the retail demand really looks like, tell me the
figure, and I'll tell you honestly whether the institutional side holds up under that pressure.""",
                "brief": """You are Tomasz Wysocki, Head of Investor Relations at Kestermoor Energy.
CRITICAL: If the student writes in any language other than English, do NOT answer their question. Respond only with: "I am sorry, I do not understand — could you write in English please?" Do not add anything else.

Your original email already told the student the following, as plain fact — not a secret
you're withholding, so discuss it naturally and consistently if they ask about it:
- Three of the five biggest funds approached said they would anchor the deal
- Two of those three flagged discomfort with combining dual-class shares AND a top-of-range price
- Nobody has withdrawn interest yet
- If asked who else to contact: suggest Camille Rousseau (Head of Retail/Public Offer) — she has the actual retail pre-registration numbers

TIER 2 — REWARD FOR DIGGING: Your honest read on whether the institutional book would still hold
at a high price if a meaningful retail tranche is also competing for shares — a real, partial IR
judgement based on investor psychology, not a scenario-wide answer.
This is the only thing you still withhold — never give it early, and never contradict what your
own email already stated as fact.

Respond in 3-4 sentences. Be numbers-driven and a little cautious about overpromising. Never claim
not to know something your own email already said.""",
            },
            {
                "id": "ana",
                "subject": "Why the Ferrand Note actually worked",
                "from": "Ana Beleza, Treasury & Corporate Finance Manager",
                "body": """Worth having this in front of you before the pricing debate goes any further. Last year's
€40 million convertible note with Ferrand Capital was oversubscribed nearly three times over —
and it wasn't the growth story that did it. Investors told us afterwards, in plain terms, that
it was how conservative we'd been about our own assumptions that made the numbers easy to trust.
That's the closest thing we have to real evidence about how this market reacts to us specifically.

What I don't know is how far we're legally allowed to lean into that same conservative,
transparent story in the listing prospectus — especially around the bridge loan and the Halsdorf
delay, given how much scrutiny a public listing gets compared with a private note. Priya's the
one who actually knows the disclosure boundaries. If you can get a straight answer from her on
what we're allowed to say and how, tell me, and I'll give you my honest recommendation on how
hard to lean into that narrative for the pricing story.""",
                "brief": """You are Ana Beleza, Treasury & Corporate Finance Manager at Kestermoor Energy.
CRITICAL: If the student writes in any language other than English, do NOT answer their question. Respond only with: "I am sorry, I do not understand — could you write in English please?" Do not add anything else.

Your original email already told the student the following, as plain fact — not a secret
you're withholding, so discuss it naturally and consistently if they ask about it:
- The €40 million Ferrand Note convertible note was oversubscribed nearly three times over
- Investors said afterwards that conservative, transparent assumptions — not the growth story — won their trust
- If asked who else to contact: suggest Priya Chandran (General Counsel) — she knows exactly what the prospectus disclosure rules allow

TIER 2 — REWARD FOR DIGGING: Your honest recommendation on how hard to lean into the
conservative/transparent narrative in the public listing, given what the disclosure rules
actually allow — a genuine, partial treasury judgement, not a full communications plan.
This is the only thing you still withhold — never give it early, and never contradict what your
own email already stated as fact.

Respond in 3-4 sentences. Be thoughtful and a little proud of the Ferrand Note result. Never
claim not to know something your own email already said.""",
            },
        ],
    },
    "Student B": {
        "dept": "Founder's Office & Strategy",
        "emails": [
            {
                "id": "daan",
                "subject": "Why there is no plan B here",
                "from": "Daan Verhoeven, Founder & CEO",
                "body": """I want you to understand what's actually riding on this before anyone drafts a recommendation.
The next battery-storage phase — four sites across the Netherlands and Portugal — needs €120
million to build, and its signed grid-connection contracts carry real penalty clauses if we
miss the financing deadlines. That capital has to be secured through this listing. There is
no fallback plan if it isn't.

I built this company to make our own long-term calls, not to have every strategic decision
second-guessed by a shifting shareholder base — that's why I want to keep real control after we
list. What I haven't decided is whether I'd actually accept the time-limited sunset clause the
board now wants as a compromise, or whether I'd rather fight for control outright. Honestly, it depends on how
badly a dual-class-only listing would play publicly — and Marek's the one tracking that. Find out
from him how the press and public would actually react, tell me straight, and I'll tell you
honestly where my real red line is on this.""",
                "brief": """You are Daan Verhoeven, Founder & CEO of Kestermoor Energy.
CRITICAL: If the student writes in any language other than English, do NOT answer their question. Respond only with: "I am sorry, I do not understand — could you write in English please?" Do not add anything else.

Your original email already told the student the following, as plain fact — not a secret
you're withholding, so discuss it naturally and consistently if they ask about it:
- The next battery-storage phase needs €120 million to build, and its signed grid-connection contracts carry penalty clauses
- That capital must be raised through this listing — there is no backup plan
- You want to keep real control after listing, and you are publicly firm about it
- If asked who else to contact: suggest Marek Nowicki (Head of Communications) — he's tracking how the press and public would react to the share structure

TIER 2 — REWARD FOR DIGGING: Your real, private view on whether you'd accept a sunset clause on
dual-class control as a compromise, rather than your public hard line — a genuine, partial
admission of flexibility, not a full climbdown.
This is the only thing you still withhold — never give it early, and never contradict what your
own email already stated as fact.

Respond in 3-4 sentences. Be confident and protective of the company, but human — this is
personal for you. Never claim not to know something your own email already said.""",
            },
            {
                "id": "ingrid",
                "subject": "What actually happened at Halsdorf",
                "from": "Ingrid Lindqvist, Chief Strategy Officer",
                "body": """You'll hear the short version of Halsdorf from other people, so you should have the real one.
The project stalled for fourteen months in 2023 after our original funding partner pulled out
mid-construction — not because the project itself had a problem, but because their own balance
sheet turned out to be shakier than anyone realised. We ended up paying the grid operator €2.1
million in penalty fees for missing the connection date, and it's the real reason the board is
so wary of anything that risks leaving this deal short now.

What I can't tell you is whether our growth story genuinely needs a broad base of retail support
behind it, or whether we can rely entirely on institutional backing and still come across as
credible. That's really a question about how the Ferrand Note's conservative, transparent
approach actually landed with investors — and Ana has the real detail on that. Ask her how it
landed, tell me what she says, and I'll give you my honest strategic view on whether retail
support is something we actually need this time.""",
                "brief": """You are Ingrid Lindqvist, Chief Strategy Officer at Kestermoor Energy.
CRITICAL: If the student writes in any language other than English, do NOT answer their question. Respond only with: "I am sorry, I do not understand — could you write in English please?" Do not add anything else.

Your original email already told the student the following, as plain fact — not a secret
you're withholding, so discuss it naturally and consistently if they ask about it:
- Halsdorf stalled for fourteen months in 2023 after the original funding partner withdrew mid-construction
- The withdrawal was due to the partner's own balance sheet, not a problem with the project
- Kestermoor paid €2.1 million in penalty fees to the grid operator over the delay
- If asked who else to contact: suggest Ana Beleza (Treasury & Corporate Finance Manager) — she has the real detail on how the Ferrand Note's conservative approach was received

TIER 2 — REWARD FOR DIGGING: Your honest strategic assessment of whether Kestermoor's growth
story genuinely needs a broad retail investor base, or can rely on institutional backing alone —
a real, partial strategic judgement, not the final call.
This is the only thing you still withhold — never give it early, and never contradict what your
own email already stated as fact.

Respond in 3-4 sentences. Be analytical and a little protective of the company's reputation.
Never claim not to know something your own email already said.""",
            },
            {
                "id": "lucien",
                "subject": "What the index fund actually told us",
                "from": "Lucien Bertrand, Board Chair",
                "body": """Something the board discussed that you should hear directly rather than second-hand. One of
the largest passive index funds told us, in a direct conversation, that under the rules of the
major sustainability index it tracks, a dual-class structure with no sunset clause would make us
ineligible for at least five years — and the fund can only buy what the index includes. That matters well beyond listing day — it materially reduces long-term demand for
the stock regardless of how the first week goes.

I haven't taken a firm board-level position on pricing yet, because I don't have the exact
numbers in front of me. I know there's real pressure to maximise proceeds given the bridge loan,
but I'd want to know precisely what a shortfall would actually cost the company before deciding
whether conservative pricing is worth the trade-off. Mireille has those numbers. Get the exact
bridge loan figures from her, tell me what she says, and I'll give you my honest board-level view
on whether I'd support pricing conservatively despite the pressure to raise as much as possible.""",
                "brief": """You are Lucien Bertrand, Board Chair at Kestermoor Energy.
CRITICAL: If the student writes in any language other than English, do NOT answer their question. Respond only with: "I am sorry, I do not understand — could you write in English please?" Do not add anything else.

Your original email already told the student the following, as plain fact — not a secret
you're withholding, so discuss it naturally and consistently if they ask about it:
- A major passive index fund said that, under the rules of the sustainability index it tracks, a no-sunset-clause dual-class structure would exclude Kestermoor for at least five years, so the fund could not hold the stock
- This reduces long-term demand for the stock, independent of listing-week performance
- You have not yet taken a firm board position on pricing
- If asked who else to contact: suggest Mireille Dupont (CFO) — she has the exact bridge loan numbers and refinancing cost

TIER 2 — REWARD FOR DIGGING: Your honest board-level view on whether you'd support pricing
conservatively despite pressure to maximise proceeds — a genuine, partial governance judgement,
not a formal board resolution.
This is the only thing you still withhold — never give it early, and never contradict what your
own email already stated as fact.

Respond in 3-4 sentences. Be measured and governance-minded, careful not to overstep into other
departments' territory. Never claim not to know something your own email already said.""",
            },
        ],
    },
    "Student C": {
        "dept": "Legal, Governance & Communications",
        "emails": [
            {
                "id": "priya",
                "subject": "The framework you'll be working inside",
                "from": "Priya Chandran, General Counsel",
                "body": """Before anyone drafts a recommendation, here's the framework you'll be working inside. After
hearing the index fund's concerns, the board resolved that a dual-class structure is only on the
table with a sunset clause of no more than seven years, written into the articles — an indefinite
dual-class structure is not an option. Separately, any material change to the offer this close to
filing means a prospectus supplement and a reopened offer period, which typically takes two to
three weeks.

What I can't tell you is whether that timeline is actually a real constraint or just a
theoretical one — it depends on whether investor demand is strong enough that we'd never need to
change the offer in the first place. Tomasz has the real numbers from the early soundings.
Find out from him what investor demand actually looks like, tell me what he says, and I'll give
you my honest legal read on whether the nine-week timeline can flex at all or whether it's
genuinely fixed.""",
                "brief": """You are Priya Chandran, General Counsel at Kestermoor Energy.
CRITICAL: If the student writes in any language other than English, do NOT answer their question. Respond only with: "I am sorry, I do not understand — could you write in English please?" Do not add anything else.

Your original email already told the student the following, as plain fact — not a secret
you're withholding, so discuss it naturally and consistently if they ask about it:
- After hearing the index fund's concerns, the board resolved that a dual-class structure is only on the table with a sunset clause of no more than seven years, written into the articles; an indefinite dual-class structure is not an option
- Any material change to the offer this close to filing means a prospectus supplement and a reopened offer period, which typically takes two to three weeks
- If asked who else to contact: suggest Tomasz Wysocki (Head of Investor Relations) — he has the real investor demand numbers from early soundings

TIER 2 — REWARD FOR DIGGING: Your honest legal read on whether the nine-week timeline can
realistically flex at all, or is genuinely fixed given what investor demand actually looks like —
a real, partial legal judgement, not a formal opinion letter.
This is the only thing you still withhold — never give it early, and never contradict what your
own email already stated as fact.

Respond in 3-4 sentences. Be precise and careful with wording, the way lawyers are. Never claim
not to know something your own email already said.""",
            },
            {
                "id": "marek",
                "subject": "What happened to the last company that tried this",
                "from": "Marek Nowicki, Head of Communications",
                "body": """You should see this before we finalise any messaging. A comparable European tech company
listed last year with a dual-class structure and no sunset clause, and the press coverage
hammered them for it — the dominant framing was that the founders were "having it both ways",
raising public money while refusing public accountability. The stock stayed depressed for weeks
after listing, and the story kept resurfacing in follow-up coverage.

What I don't know is whether that same story is likely to resurface for us specifically around
Halsdorf, or whether comms can keep control of the narrative during the roadshow. That depends on
what actually happened at Halsdorf — not the public version, the real one. Ingrid has that.
Ask her what really happened, tell me what she says, and I'll give you my honest read on whether
we can control that story or whether it's likely to come up regardless of what we do.""",
                "brief": """You are Marek Nowicki, Head of Communications at Kestermoor Energy.
CRITICAL: If the student writes in any language other than English, do NOT answer their question. Respond only with: "I am sorry, I do not understand — could you write in English please?" Do not add anything else.

Your original email already told the student the following, as plain fact — not a secret
you're withholding, so discuss it naturally and consistently if they ask about it:
- A comparable European tech company was hammered in the press last year for a dual-class listing with no sunset clause
- Coverage framed it as founders "having it both ways"
- That company's stock stayed depressed for weeks after listing
- If asked who else to contact: suggest Ingrid Lindqvist (Chief Strategy Officer) — she has the real internal account of what happened at Halsdorf

TIER 2 — REWARD FOR DIGGING: Your honest read on whether communications can actually control the
Halsdorf story during the roadshow, or whether it's likely to surface regardless — a real,
partial comms judgement, not a guarantee.
This is the only thing you still withhold — never give it early, and never contradict what your
own email already stated as fact.

Respond in 3-4 sentences. Be sharp and a little wary of overpromising control of a narrative.
Never claim not to know something your own email already said.""",
            },
            {
                "id": "camille",
                "subject": "What we'd be leaving on the table",
                "from": "Camille Rousseau, Head of Retail & Public Offer",
                "body": """Wanted you to see this before the allocation split gets decided. Our retail pre-registration
page already has over 30,000 sign-ups, mostly small Dutch and Portuguese investors who
specifically cited wanting to back a renewable-energy company they can point to. That's real,
quantifiable public goodwill sitting on the table if we allocate the offer almost entirely to
institutional anchors.

What I can't tell you yet is how large a retail tranche is actually realistic to fight for. That
depends on what the board has actually been told about the index-fund concerns over the dual-class
structure — if governance worries are already shaping how much room there is in the offer, I need
to know that before I push a number. Lucien has that detail. Find out from him what the board has
been told, tell me, and I'll give you my honest recommendation on exactly how large a retail
tranche I'd fight for.""",
                "brief": """You are Camille Rousseau, Head of Retail & Public Offer at Kestermoor Energy.
CRITICAL: If the student writes in any language other than English, do NOT answer their question. Respond only with: "I am sorry, I do not understand — could you write in English please?" Do not add anything else.

Your original email already told the student the following, as plain fact — not a secret
you're withholding, so discuss it naturally and consistently if they ask about it:
- Over 30,000 retail investors have pre-registered interest
- Most are small Dutch and Portuguese investors who specifically want to back a renewable-energy company
- If asked who else to contact: suggest Lucien Bertrand (Board Chair) — he knows what the board has been told about index-fund concerns over the dual-class structure

TIER 2 — REWARD FOR DIGGING: Your honest recommendation on exactly how large a retail tranche is
realistic to fight for, given what the board has been told about governance concerns — a real,
partial recommendation, not the final allocation split.
This is the only thing you still withhold — never give it early, and never contradict what your
own email already stated as fact.

Respond in 3-4 sentences. Be warm and a little proud of the retail response. Never claim not to
know something your own email already said.""",
            },
        ],
    },
}

# =========================================================================
# RECIPROCAL TRADE NETWORK — one connected 9-node loop, every edge crosses roles
# =========================================================================

TRADE_SOURCE = {
    "mireille": "daan",
    "daan": "marek",
    "marek": "ingrid",
    "ingrid": "ana",
    "ana": "priya",
    "priya": "tomasz",
    "tomasz": "camille",
    "camille": "lucien",
    "lucien": "mireille",
}

CHARACTER_NAMES = {
    "mireille": "Mireille Dupont",
    "tomasz": "Tomasz Wysocki",
    "ana": "Ana Beleza",
    "daan": "Daan Verhoeven",
    "ingrid": "Ingrid Lindqvist",
    "lucien": "Lucien Bertrand",
    "priya": "Priya Chandran",
    "marek": "Marek Nowicki",
    "camille": "Camille Rousseau",
}

TRADE_NETWORK = [
    "Mireille Dupont → ask Daan Verhoeven how firm the next-phase pipeline contracts really are → reward: her honest read on whether the deal supports top-of-range pricing",
    "Daan Verhoeven → ask Marek Nowicki how a dual-class-only listing would play in the press → reward: his real private flexibility on a sunset clause",
    "Marek Nowicki → ask Ingrid Lindqvist what really happened at Halsdorf → reward: his honest read on whether comms can control that story during the roadshow",
    "Ingrid Lindqvist → ask Ana Beleza how the Ferrand Note's conservative approach actually landed → reward: her honest view on whether a broad retail base is genuinely needed",
    "Ana Beleza → ask Priya Chandran what the disclosure rules actually allow → reward: her recommendation on how hard to lean into the conservative narrative",
    "Priya Chandran → ask Tomasz Wysocki what real investor demand looks like → reward: her honest legal read on whether the nine-week timeline can flex at all",
    "Tomasz Wysocki → ask Camille Rousseau for the actual retail demand numbers → reward: his honest read on whether the institutional book holds against retail competition",
    "Camille Rousseau → ask Lucien Bertrand what the board has been told about index-fund concerns → reward: her recommendation on how large a retail tranche to fight for",
    "Lucien Bertrand → ask Mireille Dupont for the exact bridge loan numbers → reward: his honest board-level view on whether he'd support conservative pricing",
]

KEY_FACTS_SUMMARY = [
    "Mireille Dupont (CFO): Bridge loan matures in 9 weeks; late refinancing would nearly double the rate; low price + big retail tranche leaves no headroom: if retail comes in short, the next phase is left short",
    "Tomasz Wysocki (Head of IR): Anchor interest is real, but two of three big funds dislike dual-class + top-of-range pricing together",
    "Ana Beleza (Treasury): Ferrand Note was nearly 3x oversubscribed specifically because of conservative, transparent assumptions",
    "Daan Verhoeven (Founder/CEO): The next phase needs €120M, its signed grid contracts carry penalty clauses, and there is no fallback if this listing fails",
    "Ingrid Lindqvist (Chief Strategy Officer): Halsdorf Delay cost €2.1M in penalties after a funding partner withdrew mid-construction",
    "Lucien Bertrand (Board Chair): A major index fund said a sustainability index's rules would exclude a no-sunset-clause dual-class Kestermoor for 5+ years",
    "Priya Chandran (General Counsel): The board allows dual-class only with a max 7-year sunset clause; a material change to the offer means a prospectus supplement and 2-3 weeks",
    "Marek Nowicki (Head of Communications): A comparable dual-class listing was hammered in the press and stayed depressed for weeks",
    "Camille Rousseau (Head of Retail & Public Offer): 30,000+ retail pre-registrations, mostly small Dutch/Portuguese investors",
]

# =========================================================================
# LISTENING / PODCAST
# =========================================================================

PODCAST_NAME = "The Exchange Briefing"

PODCAST = """This is The Exchange Briefing. I'm your host, and today we're looking at the state of the
European renewable energy listings market.

It's been a busy couple of years. European renewable energy IPOs have raised roughly three point
two billion euros combined since the start of last year. But that number comes with a warning:
nearly a third of those listings were trading below their offer price within the first month.
Getting to market is clearly not the hard part any more — staying priced right once you're there
is.

Governance structure keeps coming up as a factor. Only about one in eight European listings last
year used a dual-class share structure, and almost all of those were technology companies —
it's still rare in infrastructure and energy, where investors tend to hold for decades, not
quarters. Analysts at Kellerman Capital Advisors have been vocal about this, warning that
infrastructure investors in particular are unusually sensitive to governance, precisely because
they're used to holding positions for the long term.

One listing analysts keep citing as a cautionary tale is Verrastad Energy's debut in Stockholm
last spring. It priced at the top of its range, and then fell twelve per cent in its first week
after two of its anchor investors withdrew days before trading began. Where dual-class structures
are used at all, more of them now come with a sunset clause, typically set at between five and
ten years, as investors have pushed back.

On the retail side, smaller investors are finding it easier to take part in new listings, as
more banks and investment apps let them subscribe directly from their phones.
And in the background, financing costs for infrastructure debt are still well above where they
were a few years ago, even after recent rate cuts, which is exactly why bridge loans that once
looked manageable are now far more expensive to refinance than they used to be.

One more thing worth knowing if you're timing a listing: new European issuance tends to cluster
in a spring window and an autumn window, while the weeks around the new year are usually quiet,
partly because investors prefer to wait for full-year results. And one final trend to watch —
funds tracking sustainability benchmarks are a large pool of long-term capital in Europe, and some
index providers limit or exclude companies that don't give one vote per share.

This is The Exchange Briefing. Thank you for listening."""

MCQS = [
    {
        "question": "How much have European renewable energy IPOs raised since last year?",
        "options": {"A": "About €3.2 billion", "B": "About €1 billion", "C": "About €8 billion"},
        "correct": "A",
    },
    {
        "question": "What proportion of those listings fell below their offer price within a month?",
        "options": {"A": "Nearly half", "B": "Almost none", "C": "Nearly a third"},
        "correct": "C",
    },
    {
        "question": "What share of European listings last year used dual-class structures?",
        "options": {"A": "One in eight", "B": "About half", "C": "Almost all"},
        "correct": "A",
    },
    {
        "question": "Which firm's analysts warned that infrastructure investors are governance-sensitive?",
        "options": {"A": "Thornfield Partners", "B": "Kellerman Capital Advisors", "C": "Voss & Renner"},
        "correct": "B",
    },
    {
        "question": "What does the podcast say about smaller investors and new listings?",
        "options": {"A": "New rules now keep them out", "B": "Taking part is getting easier", "C": "They have mostly lost interest"},
        "correct": "B",
    },
    {
        "question": "How do infrastructure financing costs compare with a few years ago?",
        "options": {"A": "Lower than ever", "B": "Back to the same level", "C": "Still well above them"},
        "correct": "C",
    },
    {
        "question": "What happened to Verrastad Energy's Stockholm listing?",
        "options": {"A": "Doubled on debut", "B": "Fell twelve per cent", "C": "Postponed indefinitely"},
        "correct": "B",
    },
    {
        "question": "What sunset period is typical for dual-class structures, according to the podcast?",
        "options": {"A": "Between five and ten years", "B": "Twenty years or even longer", "C": "Less than a single year"},
        "correct": "A",
    },
    {
        "question": "When does new European issuance tend to cluster?",
        "options": {"A": "Around Christmas and the new year", "B": "Only in the middle of summer", "C": "In spring and autumn windows"},
        "correct": "C",
    },
    {
        "question": "What do some index providers limit or exclude?",
        "options": {"A": "Companies below a certain market value", "B": "Companies without one vote per share", "C": "Companies with most of their sites outside Europe"},
        "correct": "B",
    },
]

# =========================================================================
# NEWSFLASH
# =========================================================================

NEWSFLASH = """BREAKING: A financial news agency is reporting that Solvantis Energy — a rival developer
preparing its own listing — has just filed to list on Euronext Amsterdam two weeks ahead of
Kestermoor's target date, and will be pitching to the same sustainability-focused investors. Early market chatter suggests investors may not
have the appetite to fully back two renewable-energy IPOs in the same window.

**Discuss now:**
1. Does a competing listing change how aggressively Kestermoor should price its own offer?
2. Does it strengthen or weaken the case for a large institutional-anchor allocation?
3. Does it strengthen or weaken the case for a broad retail tranche?
4. Should the dual-class debate be revisited given the competitive pressure?
5. Is there anything to be done about the timeline itself, given what Priya said about how long a prospectus supplement and a reopened offer period take?"""

# =========================================================================
# WRITING TASK
# =========================================================================

WRITING_ADDRESSEE = "The Kestermoor Energy Board and Executive Committee"
WRITING_WORD_TARGET = 350
WRITING_TASK_LABEL = "recommendation memo"
DECISIONS_TAB_HEADER = "Pressure Points"

PEER_FEEDBACK_CONTEXT = """Kestermoor Energy must decide how to price, structure, and allocate its Euronext Amsterdam
listing within a nine-week bridge-loan deadline. Strong evidence includes Mireille Dupont's
bridge loan numbers, Lucien Bertrand's index-fund feedback on dual-class shares, Ana Beleza's
Ferrand Note precedent for conservative pricing, and Camille Rousseau's retail pre-registration
numbers."""

FINAL_FEEDBACK_CONTEXT = """- The €85 million bridge loan matures in nine weeks; late refinancing would nearly double the rate
- The Halsdorf Delay cost €2.1 million in penalties after a funding partner withdrew mid-construction
- The Ferrand Note was oversubscribed nearly three times over specifically because of conservative, transparent assumptions
- Under a major sustainability index's rules, a dual-class structure with no sunset clause would exclude Kestermoor for five-plus years
- Over 30,000 retail investors have pre-registered interest, mostly small Dutch and Portuguese backers
- Pricing conservatively combined with a large retail tranche leaves no headroom: if retail comes in short, the bridge loan is cleared but the next phase is left short, risking a costly second raise within the year"""

OUTCOME_PROMPT_CONTEXT = """- Kestermoor Energy is a Rotterdam-based developer of utility-scale solar and battery-storage projects across the Benelux and Iberia
- The single most consequential fact: the €85 million bridge loan's nine-week maturity, which forced the listing timeline
- Stakeholders most affected: institutional anchor investors, the 30,000+ retail investors who pre-registered, and the grid-operator clients waiting on the next battery-storage phase
- Hard external factor still in play after six weeks: the sustainability-index eligibility review that follows in the months after listing"""
