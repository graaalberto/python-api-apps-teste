CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    telefone TEXT,
    documento TEXT,
    endereco TEXT
);

CREATE TABLE IF NOT EXISTS notas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_id INTEGER NOT NULL,
    disciplina TEXT NOT NULL,
    valor REAL NOT NULL,
    semestre TEXT,
    observacao TEXT,
    FOREIGN KEY(aluno_id) REFERENCES alunos(id)
);
