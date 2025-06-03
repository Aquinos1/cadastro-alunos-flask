CREATE DATABASE IF NOT EXISTS db_escola 
CHARSET utf8mb4 COLLATE utf8mb4_general_ci;

USE db_escola;

CREATE TABLE IF NOT EXISTS tb_turma (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_aluno (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    matricula VARCHAR(50) NOT NULL UNIQUE,
    id_tb_turma INT,
    CONSTRAINT fk_tb_aluno_tb_turma FOREIGN KEY (id_tb_turma) REFERENCES tb_turma(id) ON DELETE CASCADE
);
select * from tb_aluno;
-- Exemplo de inserção de turmas
INSERT INTO tb_turma (nome) VALUES ('1º Ano A'), ('2º Ano B');
UPDATE tb_turma SET nome = 'ADS 2' WHERE id = 2;
