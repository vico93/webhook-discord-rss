# Discord RSS via Webhooks
*Tradução Português (Brasil)*

## Instruções
- Clone este repositório em uma pasta de nome à sua escolha;
- Para cadastrar um novo feed RSS no banco de dados `db.json`, rode o script `new-feed.py` e siga as instruções em tela;
  - Informações necessárias: nome do feed / nome do webhook / url do feed rss / url do webhook / url do avatar do webhook
  - Ele salvará as informações no arquivo `db.json`
- Em seguida, apenas rode o script `rss-discord.py` que irá lerá o `db.json` e verificará os feeds;
- Basta adicionar a execução do código python rss-discord.py em uma tarefa automática para que seja executado a cada x vezes

---
Original por @[Karomy404](https://github.com/Karomy404)
