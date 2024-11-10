# Pyrogram Clone Client 

## Commands
```markdown
- `/uclone <Session>`: For User Bots Cloning
- `/bclone <Token>`: For Bots Cloning
```

Follow this command format to use these commands in cloned clients.

```python
@Client.on_message(filters.command(["command"]) & filters.me)
async def example_cmd(client: Client, message: Message):
    # Your command logic here
```

𝗡𝗼𝘁𝗲: 𝗧𝗵𝗶𝘀 𝗺𝘂𝘀𝘁 𝗯𝗲 𝘂𝘀𝗲𝗱 𝘁𝗼 𝘄𝗼𝗿𝗸.



