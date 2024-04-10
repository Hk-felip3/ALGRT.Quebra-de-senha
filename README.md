            ALGORITMO DE QUEBRA DE SENHA (FORÇA BRUTA )

            SOBRE PROJETO
O código apresentado é um exemplo de um ataque de força bruta em uma senha protegida por um arquivo ZIP. Aqui está uma explicação de como o código funciona:
Importação de bibliotecas: O código importa as bibliotecas necessárias, incluindo itertools para geração de todas as combinações possíveis de caracteres da senha e time para medir o tempo de execução. A biblioteca zipfile é usada para lidar com arquivos ZIP.
Definição da função forcaBruta: Esta função recebe o arquivo ZIP, o tamanho da senha e o conjunto de caracteres possíveis. Ele utiliza a função product do itertools para gerar todas as combinações possíveis de caracteres com o tamanho especificado da senha. Em seguida, itera sobre cada senha gerada, tentando extrair o conteúdo do arquivo ZIP usando a senha. Se a senha correta for encontrada, a função retorna a senha; caso contrário, retorna None.
Definição da função verifica_senha: Esta função tenta extrair o conteúdo do arquivo ZIP usando uma senha fornecida. Se a senha estiver correta, a extração é bem-sucedida e a função retorna True. Se a senha estiver incorreta, ocorrerá uma exceção e a função imprimirá a senha incorreta no console.
Charset e tamanho da senha: O conjunto de caracteres possíveis para a senha é definido como uma string contendo dígitos de 0 a 9. O tamanho da senha é definido como 4 caracteres.
Execução do ataque de força bruta: O código cria um objeto ZipFile para o arquivo ZIP protegido com senha. Em seguida, chama a função forcaBruta passando o arquivo, o tamanho da senha e o conjunto de caracteres. Se uma senha válida for encontrada, ela será impressa junto com o tempo de execução. Caso contrário, será impressa uma mensagem indicando que a senha não pôde ser encontrada.
Em resumo, o código demonstra como realizar um ataque de força bruta em um arquivo protegido por senha, tentando todas as combinações possíveis de caracteres até encontrar a senha correta. No entanto, é importante notar que ataques de força bruta podem ser demorados e consomem muitos recursos computacionais, especialmente para senhas longas ou complexas.

            Imagem layoyt-

           TECNOLOGIA ULTILIZADA
Python: É a linguagem de programação principal utilizada neste projeto. Python é conhecido por sua simplicidade, legibilidade e vasta quantidade de bibliotecas, o que o torna uma escolha popular para uma variedade de aplicações.

Biblioteca itertools: Esta biblioteca fornece funções iteradoras para gerar combinações, permutações e outras operações sobre iteráveis. No código, ela é usada para gerar todas as combinações possíveis de caracteres para a senha.

Biblioteca time: Esta biblioteca fornece funções para trabalhar com tempo. É utilizada para medir o tempo de execução do ataque de força bruta.

Biblioteca zipfile: Esta biblioteca é usada para manipular arquivos ZIP. No código, é usada para abrir e extrair arquivos de um arquivo ZIP protegido por senha.

           REFERÊNCIAS 
Documentação oficial do Python: A documentação oficial do Python fornece informações detalhadas sobre a linguagem Python, incluindo tutoriais, guias e referências para bibliotecas padrão. Você pode acessá-la em Python Documentation.

Documentação oficial do módulo itertools: A documentação oficial do módulo itertools fornece informações sobre as funções fornecidas por esse módulo para gerar combinações, permutações e outras operações sobre iteráveis. Você pode encontrá-la em itertools — Funções iteradoras para iteráveis eficientes.

Documentação oficial do módulo zipfile: A documentação oficial do módulo zipfile oferece informações sobre como trabalhar com arquivos ZIP em Python, incluindo como criar, extrair e manipular arquivos ZIP. Você pode encontrá-la em zipfile — Trabalhando com arquivos ZIP.
