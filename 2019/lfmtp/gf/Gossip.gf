abstract Gossip = {
    cat
        Actor; Action; Stmt;
    fun
        everyone : Actor;
        someone : Actor;
        makeStmt : Actor -> Action -> Stmt;
        -- and_Sentence : Sentence -> Sentence -> Sentence;
        and : Actor -> Actor -> Actor;
}