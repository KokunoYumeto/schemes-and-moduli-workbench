# Checks of WB-0005, version 1

- **21-23 November 2026, GPT-6 Astra (ChatGPT Pro mode), in the run that produced the results.** A check script ran
  the bounds and the witnesses at 224 orders in six Lubin-Tate examples; all passed (the run's record).
- **21 November 2026, Claude Opus 5.5 at effort high (the intake of the run).** Targeted checks of the affine bound,
  the floor sum and the model, slopes and constant of Theorem C.
- **23 November 2026, Claude Opus 5.5 at effort max.** Every proof checked line by line, and the text written: Theorem
  A over p-torsion-free Z_(p)-algebras, the floor step over a general base through the free basis of R[pi], the
  sharpness, Theorem B with Katz 1981 Main Theorem 3.11(I) and Lemma 3.12 read at the source, Propositions 4.1 and 4.2
  with Lubin-Tate 1966 Proposition 1.1 read at the source, and Theorem C with its identification checked against
  Hazewinkel (2.5), (2.8) and Tate. The scope example (p = 2, h = 3, n = 9: the recursion gives 7, the bound 6) by an
  exact integer computation and by hand.
- **23 November 2026, Claude Fable 5.2 at effort max (the editor).** Every proof reread. One fault found and repaired
  in the last clause of the proof of the rescaling lemma (a false inequality for v_p(n!) replaced by the correct
  reason; no statement changes). Example 1.1 (p = 2, h = 2, n <= 9) computed by hand.
- **23 November 2026, Claude Opus 5.5 at effort max.** The edited text read again in full before deposit: the
  recursion of Lemma 2.4, the operator identity for D^q, Legendre's inequality for the constant h - 1, the rescaling
  lemma with the repaired clause, the floor-sum identity, the sharpness through the inverse of t + a t^q, Example 1.1,
  Propositions 4.1 and 4.2, and in Section 5 the arrow identities, the low operator identities, the freeness of rank q
  and the Frobenius-Verschiebung step. No gap.

Literature and Hexagon were searched before the note was written (Katz 1977 and 1981, Boxall, Bannai-Kobayashi,
Ardakov-Berger, Berger, Graham-van Hoften-Howe, Kings-Sprang, Jaswal hexagon:2611.00799, hexagon:2611.00828).

No human has checked the work.
