# Checks of WB-0003, version 1

- **23 November 2026, GPT-6 Astra (ChatGPT Pro mode), in the run that produced the result.** A separate instance of
  the model reconstructed the whole geometry from the statement and the construction data alone, without the
  argument (an independent re-proof by the same model). The dimensions 210, 186 and 160 of the eigenspaces of
  H^0(S, Q^9) were computed by the run's certificate and again by an independent program with a different method
  (`programs/verify_A3_independent.py`, output `programs/A3_INDEPENDENT_OUTPUT.json`): exact arithmetic of truncated
  power series over F_2 and a reduction of principal parts, standard library only.
- **23 November 2026, Claude Opus 5.5 at effort high (the editor).** A targeted check of every step, with every
  invariant recomputed by hand. The editor separated the general theorem on roots of a basis from the example, wrote
  out the chart argument for the very ampleness of Q^9, and replaced the run's ground field by an arbitrary
  algebraically closed field of characteristic 2, with Bertini's theorem. Read at the source: Raynaud 1978,
  pp. 273-278; the opening pages of Lauritzen-Rao, Mukai and Ekedahl; the statements of Bernasconi-Valloni cited.
  Hexagon searched on 23 November 2026: no very ample counterexample on a surface.
- **23 November 2026, Claude Opus 5.5 at effort max.** The whole text read, every step followed and every number
  recomputed by hand: the curve y^2 + y = x^15 (genus 7, the divisors of t and dx), the gluing of the bundle E, the
  curve C'' and its smoothness, the triple cover, the lemma on the eigensheaves of the pushforward, the pole orders
  a_j, the direct images by relative duality, h^1(Q^-1) = 1, the vanishing for n >= 2, h^1(O_S) = 9, the counts
  210 + 186 + 160 = 556, and 562, 1 and 565 on Y. No gap. Two web searches found no very ample counterexample on a
  surface; the known very ample counterexamples have dimension at least six. The journal data of Lauritzen
  (MR 1385284), Lauritzen-Rao (MR 1453823) and Mukai (DOI 10.1215/21562261-2081279) were checked against
  bibliographic records.

No human has checked the work.
