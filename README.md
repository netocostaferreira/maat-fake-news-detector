# maat-fake-news-detector
<img src="https://user-images.githubusercontent.com/39732319/185807965-a1b47ed5-392c-4efd-b199-06d64271402d.jpg" width="1000" height="300">

<table>
<tr>
<td>
 MA'AT (nome da deusa egípcia da verdade, justiça, retidão e ordem) é uma ferramenta baseada em estratégias de NLP (Natural Language Processing) e machine learning, tendo por objetivo analisar e classificar notícias - <b>EM LÍNGUA INGLESA E ASSOCIADAS À ELEIÇÃO ESTADUNIDENSE DE 2020 (BIDEN vs TRUMP)</b> - como, potencialmente, 'verdadeiras' ou 'falsas'. MAAT foi treinado a partir de banco de dados balanceado, contendo, aproximadamente, 7000 instâncias de notícias verdadeiras ou falsas. Como output, o usuário recebe uma sentença classificando a notícia escrutinada e a probabilidade desse output estar correto.
</td>
</tr>
</table>


## Como MA'AT foi obtido?
A acurácia do MA'AT (a implementação resultante tem acurácia de cerca de 90%) é oriunda do escrutínio de três diferentes modelos:
- Regressão logística (RegLog); 
- C-Support Vector Classification (SVC); 
- Long short-term memory (LSTM), uma rede neural. 
<p> Para o volume de dados analisado, o modelo <b>RegLog </b>apresentou superioridade em relação aos demais. Esse, portanto, foi implementado como modelo de produção. Futuramente, novas melhorias - dentre essas, novo modelos - podem ser adicionadas à plataforma obtida.</p>


## [Site](https://maat-fake-news-detector.herokuapp.com/) 

### Página inicial:

![Captura de tela de 2022-08-20 09-31-39](https://user-images.githubusercontent.com/39732319/185808118-ea2ac614-0b4b-453d-a7e0-9f4f6dd3f47f.png)

### Seção da página inicial onde a notícia será analisada:
![Captura de tela de 2022-08-20 09-48-12](https://user-images.githubusercontent.com/39732319/185808157-f2b0efc3-6615-4094-8a84-8fb202b3bf62.png)

## Suporte para mobile:
O WebApp é compatível com dispositivos de todos os tamanhos e sistemas operacionais.
<p align="center">
<img src="https://user-images.githubusercontent.com/39732319/185808265-4748e3f9-2e07-44cb-8f57-66e6733f5d41.jpg" width="350" height="640">
</p>

## Uso 

### Desenvolvimento e melhorias:
Quer contribuir? Excelente!

Para corrigir um bug ou aprimorar um módulo existente, por favor, siga estas etapas:

- Fork o repositório
- Crie uma nova branch (git checkout -b melhore-recurso)
- Faça as alterações apropriadas nos arquivos
- Adicione alterações para refletir as alterações feitas
- Confirme suas alterações (git commit -am 'Melhorar recurso')
- Push para a branch (git push origin improve-feature)
- Crie um pull request

### Bug / Feature Request:

- Caso encontre um bug (o site não conseguiu lidar com a query e/ou deu resultados indesejados), abra um requerimento [aqui](https://github.com/netocostaferreira/maat-fake-news-detector/issues) incluindo sua query e o resultado esperado.

- Caso queria solicitar uma nova função, sinta-se à vontade para fazê-lo abrindo um requerimento [aqui](https://github.com/netocostaferreira/maat-fake-news-detector/issues). Inclua queries de amostra e seus resultados correspondentes.


## Construído com: 

- [Flask](https://flask.palletsprojects.com/en/2.2.x/) 
- [Sklearn](https://scikit-learn.org/stable/) 
- [Keras](https://keras.io/)
- [Google colab](https://colab.research.google.com/) 


## Licença:

MIT © [Neto Costa Ferreira ](https://github.com/netocostaferreira) | netocostaferreira@gmail.com

