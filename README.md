## Instruções de como rodar

*Observações: Todas as instruções foram feitas utilizando Terminal Bash no Windows.*

Primeiramente baixe o UV substituto para o PIP, que é muito melhor, através do comando:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Após fazer um Fork do reposítório você vai iniciar uma máquina virtual para armazenar as bibliotecas do projeto. Através do código:

```
uv venv venv
source venv/Scripts/activate
```
Após isso você vai fazer o Download das dependências, através do comando:

```
uv pip install -r requirements.txt
```
Após isso basta rodar o código abaixo para que o video com a identificação dos rostos já seja exibido.

Identificação de rostos
```
python CNN.py
```

Identificação de Emoções/ Sorissos (Pergunta 3)
```
python HAAR.py
```
---
## Respostas para as perguntas:

### Pergunta 1
O método utilizado para a identificação dos rostos no meu código foi o Convolutional Neural Network (CNN), que consiste em uma rede neural que se utiliza de neurônios artificiais que através de pesos vão alterando o input dado para chegar no melhor resultado possível. Entretando nesse modelo em especifico também existe uma camada aonde é feito um processo de convolução, o que reduz a complexidade do modelo e o número de parâmetros, otimizando assim a aplicação.

### Pergunta 2
Hierarquisando as soluções oferecidas, colocaria nas seguintes posições.
- CNN e Filtros de correlação Crusada
- HAAR Cascade
- NN Linear


Coloquei em primeiro lugar o CNN e o Filtro CC, pois ambos são muito parecidos com uma pequena difença que enquanto o CNN utiliza da convolução como uma de suas camadas o Filtro de CC utiliza uma cada de correlação cruzada que apresenta resultados muito similáres com a de convolução. 

Em segundo coloco o HAAR Cascade uma vez que ele faz um bom trabalho em identificar maior parte das faces porém ainda com algumas inconsistências e dificuldades.

E Por último o NN Linear pelo motivo que é muito mais eficiente em problemas de classificação que não envolve mais de 1 dimensão o que o torna menos eficiente para trabalhar com imagens.

### Pergunta 3 
Implementei um HAAR cascade que para roda-lo é apenas executar o código:
```
python HAAR.py
```
Aonde ele tenta identificar os olhos e o sorriso das pessoas sendo assim possível identificar emções através de pequenas variações dessas partes identificadas.
### Pergunta 4
Acho que isso seria possível sim entretanto teria que ser feita uma relação de dependência entre os frames e eles herdarem informações dos anteriores para ter classificações mais precisas, mas além do mais é possível usar vários modelos fazendo predições ao mesmo tempo assim como eu fiz com HAAR, aonde tem um focado nos olhos e outro no sorriso, isso já ajuda a decifrar padrões mais complexos no final das contas.
