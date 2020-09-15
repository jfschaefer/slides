abstract Gossip = {
  cat
    Actor;
    Action;
    Stmt;
  fun
    everyone : Actor;
    someone  : Actor;
    makeStmt :
          Actor->Action->Stmt;
    twoOf:Actor->Actor->Actor;
}
