from telethon import events, Button


async def start_srb(event, st):
    await event.reply(st, 
                      buttons=[
                              [Button.url("🦋 ᴜᴘᴅᴀᴛᴇ", url="https://t.me/Opleech"),
                               Button.url("🦋 sᴜᴘᴘᴏʀᴛ", url="https://t.me/WD_Topic_Group")],
                              [Button.url("𝐖𝐎𝐎𝐃𝐜𝐫𝐚𝐟𝐭", url="t.me/Farooq_is_KING")],
                              [Button.url("𝐖𝐎𝐎𝐃𝐜𝐫𝐚𝐟𝐭,𝐬 𝐁𝐨𝐭", url="t.me/WD_Contact_Bot")]]) 
    
async def vc_menu(event):
    await event.edit("**VIDEO CONVERTOR v1.4**", 
                    buttons=[
                        [Button.inline("info.", data="info"),
                         Button.inline("SOURCE", data="source")],
                        [Button.inline("NOTICE.", data="notice"),
                         Button.inline("Main.", data="help")],
                        [Button.url("𝐖𝐎𝐎𝐃𝐜𝐫𝐚𝐟𝐭", url="t.me/Farooq_is_KING")]])
    
