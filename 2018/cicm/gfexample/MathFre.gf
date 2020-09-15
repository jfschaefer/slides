concrete MathFre of Math = open SyntaxFre, ParadigmsFre in {
  lincat
    Object = CN;        -- common noun
    Property = AP;      -- adjective phrase
    Statement = S;      -- sentence
  lin
    group = mkCN (mkN "groupe" masculine);
    abelian = mkAP (mkA "abélien");
    commutative = mkAP (mkA "commutatif");
    addProperty prop obj = mkCN prop obj;
    hasProperty obj prop = mkS (mkCl (mkNP aSg_Det obj) prop);
}
