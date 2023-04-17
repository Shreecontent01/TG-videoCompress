#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .
from decouple import config
try:
    APP_ID = config("APP_ID", default=7868296, cast=int)
    API_HASH = config("API_HASH", default="bfa7fecb33443243ff8c8b0f27f9cd68")
    BOT_TOKEN = config("BOT_TOKEN", default="5896665703:AAEoqSzLV7l5BxlImlHyEXEBDKM1NY2aQ_4")
    DEV = 1322549723
    OWNER = config("OWNER", default=5012158248 )
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -preset ultrafast -c:v libx265 -crf 27 -map 0:v -c:a aac -map 0:a -c:s copy -map 0:s? "{}"',
    )
    THUMB = config(
        "THUMBNAIL", default="https://te.legra.ph/file/9c245e214cfdadf167e13.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
