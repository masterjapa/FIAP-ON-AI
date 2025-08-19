# FIAP ON - AI

Repositório para projetos e atividades do curso FIAP ON de Inteligência Artificial.

## Estrutura do Projeto

- **ia-e-seu-mundo-de-possibilidades/** - Atividade sobre detecção de utensílios com Teachable Machine
- **play-na-sua-carreira-em-ia/** - Projeto FarmTech Solutions com Python e R

## Como Colaborar no Projeto

Este guia foi criado especialmente para quem nunca trabalhou com Git e GitHub antes. Vamos explicar passo a passo como contribuir com este projeto.

### O que você vai aprender

- Como fazer uma cópia do projeto (Fork)
- Como baixar o projeto no seu computador (Clone)
- Como criar sua própria versão (Branch)
- Como enviar suas mudanças (Commit e Push)
- Como solicitar que suas mudanças sejam incluídas (Pull Request)

### Passo a Passo para Colaborar

#### 1. Fazendo um Fork (sua cópia pessoal do projeto)

O **Fork** cria uma cópia do projeto na sua conta do GitHub.

1. Acesse o repositório original no GitHub
2. Clique no botão **"Fork"** no canto superior direito
3. Aguarde a criação da cópia
4. Agora você tem sua própria versão do projeto!

#### 2. Clonando o Repositório (baixando para seu computador)

O **Clone** baixa o projeto do GitHub para seu computador.

```bash
# Substitua SEU_USUARIO pelo seu nome de usuário do GitHub
git clone https://github.com/SEU_USUARIO/FIAP-ON-AI.git

# Entre na pasta do projeto
cd FIAP-ON-AI
```

#### 3. Criando uma Branch (sua área de trabalho)

A **Branch** é como uma pasta separada onde você faz suas mudanças sem afetar o código principal.

```bash
# Crie e mude para uma nova branch
# Use um nome descritivo para sua branch
git checkout -b minha-nova-funcionalidade

# Exemplos de bons nomes de branch:
# git checkout -b adicionar-calculo-area
# git checkout -b corrigir-bug-menu
# git checkout -b atualizar-documentacao
```

#### 4. Fazendo suas Alterações

Agora você pode:
- Editar arquivos existentes
- Criar novos arquivos
- Adicionar suas implementações
- Corrigir bugs

Use seu editor de código favorito (VS Code, PyCharm, etc.)

#### 5. Salvando suas Mudanças (Commit)

O **Commit** salva suas mudanças com uma mensagem explicativa.

```bash
# Veja quais arquivos foram modificados
git status

# Adicione os arquivos modificados
git add .
# Ou adicione arquivos específicos
git add nome_do_arquivo.py

# Salve as mudanças com uma mensagem clara
git commit -m "Adiciona nova funcionalidade"

# Exemplos de boas mensagens de commit:
# "Adiciona nova funcionalidade X"
# "Corrige bug na função Y"
# "Atualiza documentação do módulo Z"
```

#### 6. Enviando para o GitHub (Push)

O **Push** envia suas mudanças do computador para o GitHub.

```bash
# Envie sua branch para o GitHub
git push origin minha-nova-funcionalidade
```

#### 7. Criando um Pull Request (PR)

O **Pull Request** é como você pede para que suas mudanças sejam incluídas no projeto principal.

1. Acesse seu fork no GitHub
2. Você verá uma mensagem sobre sua branch recém-enviada
3. Clique em **"Compare & pull request"**
4. Preencha o formulário:
   - **Título**: Descreva brevemente o que você fez
   - **Descrição**: Explique detalhadamente:
     - O que foi alterado
     - Por que foi alterado
     - Como testar as mudanças
5. Clique em **"Create pull request"**

### Boas Práticas para Iniciantes

#### Faça

- **Commits pequenos e frequentes**: Melhor vários commits pequenos do que um gigante
- **Mensagens claras**: Explique O QUE mudou e POR QUE
- **Teste seu código**: Certifique-se de que tudo funciona antes de enviar
- **Leia os comentários**: Se alguém sugerir mudanças no seu PR, implemente-as
- **Pergunte quando tiver dúvidas**: Não tenha medo de pedir ajuda

#### Evite

- **Commits com mensagens vagas**: "alterações", "update", "fix"
- **Enviar código que não funciona**: Sempre teste antes
- **Fazer muitas coisas em um PR**: Um PR = uma funcionalidade ou correção
- **Ignorar o feedback**: As sugestões ajudam você a melhorar

### Mantendo seu Fork Atualizado

Quando outras pessoas contribuem, você precisa atualizar sua cópia:

```bash
# Adicione o repositório original como "upstream"
git remote add upstream https://github.com/USUARIO_ORIGINAL/FIAP-ON-AI.git

# Busque as atualizações
git fetch upstream

# Mude para sua branch main
git checkout main

# Incorpore as mudanças
git merge upstream/main

# Envie para seu fork
git push origin main
```

### Comandos Úteis do Git

```bash
# Ver o status atual
git status

# Ver o histórico de commits
git log --oneline

# Ver as mudanças não salvas
git diff

# Voltar para a branch principal
git checkout main

# Listar todas as branches
git branch -a

# Deletar uma branch local
git branch -d nome-da-branch

# Desfazer mudanças em um arquivo
git checkout -- nome_do_arquivo.py

# Ver configuração do Git
git config --list
```

### Checklist Antes do Pull Request

- [ ] Meu código está funcionando sem erros
- [ ] Testei todas as funcionalidades que alterei
- [ ] Adicionei comentários onde necessário
- [ ] Minha mensagem de commit é clara
- [ ] Atualizei a documentação se necessário
- [ ] Meu código segue o padrão do projeto

### Recursos para Aprender Mais

- [Git - Guia Prático](https://rogerdudler.github.io/git-guide/index.pt_BR.html)
- [GitHub para Iniciantes](https://guides.github.com/activities/hello-world/)
- [Curso Gratuito de Git e GitHub](https://www.youtube.com/watch?v=xEKo29OWILE&list=PLHz_AreHm4dm7ZpyrSRVjz29mKR1CecQ-)
- [Documentação Oficial do Git](https://git-scm.com/book/pt-br/v2)

### Perguntas Frequentes

**P: Fiz algo errado, como desfaço?**
R: Use `git status` para ver o que mudou e `git checkout -- arquivo` para desfazer mudanças não salvas.

**P: Como sei se meu PR foi aceito?**
R: Você receberá uma notificação no GitHub e por email quando houver atividade no seu PR.

**P: Posso fazer mudanças depois de criar o PR?**
R: Sim! Basta fazer novos commits na mesma branch e dar push. O PR será atualizado automaticamente.

**P: O que é "merge conflict"?**
R: Acontece quando duas pessoas mudam a mesma parte do código. Peça ajuda para resolver!

---

**Lembre-se**: Todo mundo já foi iniciante! Não tenha medo de errar, faz parte do aprendizado. A comunidade está aqui para ajudar!

## Contato e Suporte

Se tiver dúvidas sobre colaboração:
1. Abra uma [Issue](https://github.com/SEU_USUARIO/FIAP-ON-AI/issues) no GitHub
2. Pergunte no grupo do projeto
3. Consulte a documentação acima

Boa sorte com suas contribuições!