concrete MathEng of Math = open SyntaxEng, ParadigmsEng in {
  lincat
    Object = CN;        -- common noun
    Property = AP;      -- adjective phrase
    Statement = S;      -- sentence
  lin
    group = mkCN (mkN "group");
    abelian = mkAP (mkA "Abelian");
    commutative = mkAP (mkA "commutative");
    addProperty prop obj = mkCN prop obj;
    hasProperty obj prop = mkS (mkCl (mkNP aSg_Det obj) prop);
}
