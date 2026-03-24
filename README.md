# The Satellite Project

The Satellite Project is a reimagination of the late Harbinger Satellite Roblox Project, but in Discord this time.

At its core, this project lets multiple Discord servers bind a channel to a shared satellite network, allowing relays between subscribed servers.

## Unlike the Harbinger Satellite Project

The Satellite Project is open source.

That means:

- anyone can read the source
- anyone can self-host their own instance
- anyone can run their own private satellite network
- anyone can contribute improvements to the project

This project is meant to be something people can actually take, run, modify, and build on themselves.

## Why There Is No Public Instance

There will not be a public instance of the bot.

Because a satellite network can be connected to any server where the bot can be used by someone with `Manage Channels`, a public shared instance would introduce privacy and trust problems.

In short: self-hosting is the intended model.

## Features

- Cross-server relay system for subscribed channels
- Per-server bind, rebind, unbind, connect, and disconnect controls
- Optional webhook-based relays for cleaner message presentation
- Redis-backed subscription storage
- Hybrid commands, so both slash commands and prefix commands work

## Tech Stack

- Python 3.12
- `discord.py`
- Redis

## Self-Hosting

### 1. Clone the repository

```bash
git clone https://github.com/Encythes-Works/The-Satellite-Project.git
cd The-Satellite-Project
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy [`.env.example`](/E:/Projects/Python/The-Satellite-Project/.env.example) to `.env` and fill in the values:

```env
DISCORD_TOKEN=your-discord-bot-token
REDIS_URL=redis://localhost:6379/0
COMMAND_PREFIX=$>
COMMAND_SYNC_MODE=guild
DEV_GUILD_ID=
```

What these do:

- `DISCORD_TOKEN`: your bot token from the Discord Developer Portal
- `REDIS_URL`: where Redis is running
- `COMMAND_PREFIX`: the text command prefix, currently `$>`
- `COMMAND_SYNC_MODE`: slash-command sync mode
- `DEV_GUILD_ID`: your test server id for fast development sync

### 5. Start Redis

If you already have Redis installed locally, you can use that.

Otherwise:

```bash
docker compose up -d redis
```

### 6. Run the bot

```bash
python main.py
```

## Inviting the Bot

To add your own instance to a server, generate an OAuth2 URL in the Discord Developer Portal.

Scopes you will usually want:

- `bot`
- `applications.commands`

Permissions the bot should have:

- `View Channels`
- `Send Messages`
- `Read Message History`
- `Manage Webhooks`

`Manage Webhooks` is only needed if you want webhook-based relay formatting.

If your bot is not marked as a public bot, you can still add it to your own servers through the OAuth2 install flow as the application owner.

## Command Sync

Hybrid commands have two sides:

- prefix commands update immediately on restart
- slash command availability depends on command tree sync

Recommended modes:

- `COMMAND_SYNC_MODE=guild`: best for development
- `COMMAND_SYNC_MODE=global`: use when you want to publish globally
- `COMMAND_SYNC_MODE=none`: skip slash syncing for that run

For fast iteration:

```env
COMMAND_SYNC_MODE=guild
DEV_GUILD_ID=your_test_server_id
```

## Core Commands

Current commands include:

- `$>bind` / `/bind`: bind the current channel to the satellite network
- `$>rebind` / `/rebind`: move the satellite channel to the current channel
- `$>unbind` / `/unbind`: remove this server from the network
- `$>connect` / `/connect`: reconnect a previously disconnected subscription
- `$>disconnect` / `/disconnect`: disconnect a subscription without unbinding it
- `$>network` / `/network`: show the servers currently on the network
- `$>ping` / `/ping`: simple bot health check

## How the Network Works

Each subscribed server stores:

- the subscribed channel id
- whether the subscription is active
- an optional webhook URL

When a user sends a normal message in that subscribed channel:

- the bot checks whether that server is connected
- the message is relayed to other connected subscriptions
- if a destination has a webhook configured, the relay uses it
- otherwise, the relay is sent as a normal bot message

## Project Layout

- [main.py](/E:/Projects/Python/The-Satellite-Project/main.py): local entrypoint
- [src/main.py](/E:/Projects/Python/The-Satellite-Project/src/main.py): bot startup, sync, and relay logic
- [src/commands](/E:/Projects/Python/The-Satellite-Project/src/commands): command modules
- [src/redis_client.py](/E:/Projects/Python/The-Satellite-Project/src/redis_client.py): Redis subscription storage
- [src/webhook_manager.py](/E:/Projects/Python/The-Satellite-Project/src/webhook_manager.py): webhook creation and reuse

## Transparency

This is the first project where agentic coding has been used as part of development here, specifically with Codex.

That is unusual compared to the structure of many other projects I have worked on, and that difference is reflected in the layout and workflow of this repository.

## GitHub

Project repository:

[The Satellite Project](https://github.com/Encythes-Works/The-Satellite-Project)
