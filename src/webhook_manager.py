from __future__ import annotations

import discord
from discord.ext import commands

WEBHOOK_NAME = "Satellite Webhook"

async def find_existing_webhook(bot: commands.Bot, channel: discord.TextChannel) -> discord.Webhook | None:
    me = channel.guild.me
    if me is None:
        member = channel.guild.get_member(bot.user.id) if bot.user is not None else None
        me = member

    if me is None:
        raise RuntimeError("The bot member could not be resolved for this guild.")

    permissions = channel.permissions_for(me)
    if not permissions.manage_webhooks:
        raise RuntimeError("I need the Manage Webhooks permission in this channel.")

    existing_webhooks = await channel.webhooks()
    for webhook in existing_webhooks:
        if webhook.user is not None and bot.user is not None and webhook.user.id == bot.user.id:
            return webhook

    return None

async def get_webhook(bot: commands.Bot, channel: discord.TextChannel) -> discord.Webhook:
    existing_webhook = await find_existing_webhook(bot, channel)
    if existing_webhook: return existing_webhook
    
    return await channel.create_webhook(name=WEBHOOK_NAME)

async def delete_webhook(bot: commands.bot, channel: discord.TextChannel) -> bool:
    existing_webhook = await find_existing_webhook(bot, channel)
    if existing_webhook is None:
        return False
    
    await existing_webhook.delete()
    return True