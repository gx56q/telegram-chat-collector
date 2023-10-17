import asyncio
import secrets
from pyrogram import Client


api_id = secrets.api_id
api_hash = secrets.api_hash
phone = secrets.phone
limit = secrets.limit
chat_id = secrets.chat_id


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        users_list = []
        async for member in app.get_chat_members(chat_id):
            print('@'+member.user.username)
            users_list.append('@'+member.user.username)

    with open('users.txt', 'w') as f:
        for item in users_list:
            f.write("%s " % item)
    print(len(list))


if __name__ == '__main__':
    asyncio.run(main())
