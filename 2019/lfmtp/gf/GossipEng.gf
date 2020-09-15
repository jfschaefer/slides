concrete GossipEng of Gossip = {
    param
        Plurality = Sg | Pl;
    lincat
        Actor = {s : Str; p : Plurality};
        Action = Plurality => Str;
        Stmt = Str;
    lin
        everyone = {s = "everyone"; p = Sg};
        someone = {s = "someone"; p = Sg};
        makeStmt actor action = actor.s ++ action ! actor.p;
        -- and_Sentence a b = a ++ "and" ++ b;
        and a b = {s = a.s ++ "and" ++ b.s; p = Pl};
}