# Selenium Automation For WhatsApp | Automação em Selenium para WhatsApp <img src="https://user-images.githubusercontent.com/86479393/183928445-99b6bbd0-d1dc-4a90-840e-22d2459fc888.png" width="40" height="40"><img src="https://user-images.githubusercontent.com/86479393/183930239-50cb98a4-49e3-42c6-b38b-88ccbebc9395.png" width="40" height="40"><img src="https://user-images.githubusercontent.com/86479393/183930853-bd8bc5de-c1b4-4a8f-a302-23880b31ad7c.png" width="40" height="40"> 

## Pré-requisitos
1. requirements.txt
2. ChromeDriver == 104.0.5112.79 (https://chromedriver.chromium.org/downloads) - Caso a versão do seu Google Chrome seja 104.0.5112.79.
Para erros de incompatibilidade do chromedriver, verifique, no código, o erro e a versão, a qual esta sendo pedida vá ao link e baixe a versão correta.
3. Python == 3.10.4

## Síntese
  `O programa consiste em`: Pegar **Número** e ***DDD*** de celulares, a partir de um arquivo, e mandar de forma automática mensagens com/sem fotos para esses contatos no WhatsApp.  

## Instruções

```ruby
# Caso não queira mandar imagens, mudar True para False
74 imagem = True
```

```ruby
# Número tem que ser string e no formato XXXXXXXX, ou seja, apenas os números, sem o "9" ou o "DDD"
92 numero = df["Numero"].iloc[i]
# DDD tem que ser string e no formato XX, ou seja, sem o "0" na frente.
93 ddd = df["DDD"].iloc[i]
```

```ruby
# Escreva aqui a frase a ser mandada para cada contato
115 frase_desejada = ''
```


## Recomendações

- Filtrar os números e ddds antes de alimentar para o programa, ou seja, retirar valores nulos, formatá-los e etc.
- Caso utilize instancias aws/google não utilizar de programas como VSCODE ou análogos, simplificar para o uso de arquivos executáveis devido a utilização de RAM.
- Não utilizar o computador enquanto estiver rodando o código pois, pode atrapalhar o funcionamento dele.
- Prestar atenção nos diretórios dos "paths" para imagem ou chromedriver.
