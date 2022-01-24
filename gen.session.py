import asyncio
from pyrogram import Client as c

API_ID = input("\nMasukkan API ID milikmu :\n > ")
API_HASH = input("\nMasukkan API HASH milikmu :\n > ")

print("\n\nMasukkan Nomor HP jika ditanya.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    print("\nIni adalah STRING_SESSION milikmu, jangan disebar!!\n")
    print(f"\n{ss}\n")


asyncio.run(main())
