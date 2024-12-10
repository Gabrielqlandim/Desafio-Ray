<h1>Desafio-Ray</h1>
<p>Seleção de estágio para a Ray Consulting</p>

<h2>Projeto</h2>
<p>
    Foi criada uma aplicação que busca, por meio de uma chave API do YouTube no Google Cloud, as informações da playlist de melhores momentos da Fórmula 1 em 2024 no YouTube. 
    Na utilização da biblioteca no meu código, usei funções que são da própria biblioteca, como <code>videos()</code> e <code>playlistItems()</code> e usei tbm a biblioteca pandas que contém funções, como a <code>ExcelWriter</code>, que pegam os dados da minha API em python para jogar eles em um arquivo excel que contém graficos de vizualização e curtidas de todos os videos.
</p>
<p>
    Minha lógica consistiu em usar uma função para extrair os dados de cada vídeo, assim tornando o código mais fácil de entender e mais organizado.
</p>

<h2>Principais Desafios</h2>
<p>
    Este foi o meu primeiro contato com o desenvolvimento de uma aplicação que consome APIs e também meu primeiro contato com um dashboard. Enfrentei desafios como:
</p>
<ul>
    <li>Entender o funcionamento da API do YouTube.</li>
    <li>Aprender a configurar e usar bibliotecas como <code>googleapiclient</code>.</li>
    <li>Estruturar o código para extrair e organizar os dados corretamente.</li>
    <li>Pesquisar formas de lidar com erros e construir uma lógica funcional.</li>
    <li>Aprender a fazer um codigo automatizado em python que lance os dados retirados dele direto para um dashboard em excel.</li>
    <li>Entender o funcionamento da biblioteca pandas no python.</li>
</ul>
<p>Para superar essas dificuldades, recorri a:</p>
<ul>
    <li>Tutoriais no YouTube.</li>
    <li>Fóruns e comunidades, como o Stack Overflow.</li>
    <li>A documentação oficial da API do YouTube.</li>
    <li>A documentação oficial da biblioteca xlswriter.</li>
</ul>

<h2>Como rodar</h2>
<ol>
    <li>Clone o repositório.</li>
    <li>Insira sua chave de API no local indicado no código.</li>
    <li>Execute o script clicando em <code>RUN</code>.</li>
    <li>Depois que rodar, aparecerá um arquivo excel, nele haverá o dashboard com os dados. Para conseguir ver, tem que abrir esse arquivo no excel.</li>
</ol>
