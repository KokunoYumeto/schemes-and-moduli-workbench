# WB-0008, version 1: the checks

Every check is listed by statement in `CHECK_EVENTS.tsv`. In short:

- **21 November 2026, Claude Opus 5.5 at effort max.** Independent re-proofs of the normal form (Lemma 3.1), the
  ideals, primes and topology of the spectrum (Theorem 1), the product decomposition (Remark 3.3), the description of
  semimodules (Theorem 2), the lemma on retracts of Boolean lattices (Lemma 5.1) and the classification of
  projectives (Theorem 3). Exact computations by `checks/h22_checks.py` (pure Python; its output is
  `checks/h22_checks_output.txt`): the ideals and prime ideals of (Z/n)_0 for n = 2, 3, 4, 5, 6, 8, 9, 12; (Z/6)_0 as
  the fibre product (Z/2)_0 x_B (Z/3)_0; 80 random subsemimodules of (F_p)_0^n (p = 2, 3; n = 2..4), not built from
  diagrams, decomposed as Theorem 2 says; and all idempotent join-endomorphisms of P([n]), n <= 4, have distributive
  images (Lemma 5.1).
- **23 November 2026, Claude Opus 5.5 at effort max.** The classification of congruences (Theorem 1(c)) and the
  results of Section 6 proved in the generality given.
- **23 November 2026, Claude Fable 5.2 at effort max (editor).** Every proof followed line by line. One step repaired:
  in the "if" part of Theorem 3 the free modules R^{n_j} must have n_j >= 1. Added, with proofs: Corollary 4,
  Proposition 5.3, Remarks 3.3 and 4.2, the description of the open sets in Theorem 1, and the examples.
- **23 November 2026, Claude Opus 5.5 at effort max.** The edited text read in full and every proof followed: no gap.
  Caviglia, Faul, Manuell and Mesiti (arXiv:2607.12944v2) read at the source; the text credits their Theorem 8.5.
- **24 November 2026.** GPT-6 Astra (ChatGPT Pro mode), in a later research run, found two sentences of the draft
  false: an R-module is projective over R_0 only if it is zero. Claude Fable 5.2 at effort max confirmed it; Claude
  Opus 5.5 at effort max corrected the text and proved the corrected statement (Remark 5.4). The bibliographic data
  of the references cited from memory were checked against Crossref.

No human has checked the proofs.
