CREATE TABLE estacionamento(
    id SERIAL PRIMARY KEY,
    veiculo VARCHAR(9) NOT NULL,
    tempo INT NOT NULL,
    valor NUMERIC CHECK(valor > 0)NOT NULL
);