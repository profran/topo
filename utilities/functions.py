import discord
import asyncio

def contains_not_allowed_characters(message):

    if (message.author.id != '434538091781292032'):

        not_allowed_characters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

        for char in message.content:

            for not_allowed in not_allowed_characters:

                if(char == not_allowed):

                    return True

        return False
