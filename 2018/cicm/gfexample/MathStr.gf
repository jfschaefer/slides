concrete MathStr of Math = {
  lincat
    Object = Str;
    Property = Str;
    Statement = Str;
  lin
    group = "group";
    abelian = "Abelian";
    commutative = "commutative";
    addProperty prop obj = prop ++ obj;
    hasProperty obj prop = "an" ++ obj ++ "is" ++ prop;
}
