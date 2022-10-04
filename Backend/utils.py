import hashlib
import pathlib
import random

import aiofiles

from DTOs.book_dto import BookDtoObsolete, BookDto
from DB.models import Book

DIR = pathlib.Path(__file__).parent.resolve()


def md5_file_decsr(f) -> str:
    hash_md5 = hashlib.md5()
    for chunk in iter(lambda: f.read(4096), b""):
        hash_md5.update(chunk)
    return hash_md5.hexdigest()


def md5(fname) -> str:
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def get_book_dto(book: Book) -> BookDto:
    # url = book.bookfile.path
    url = f"reader/{book.bookfile.path}"
    return BookDto(id=book.id,
                   title=book.title,
                   last_read_page=book.last_read_page,
                   file_url=url)
    # with open(book.bookfile.path, "rb") as content:
    #     return BookDto(id=book.id,
    #                    title=book.title,
    #                    last_read_page=book.last_read_page,
    #                    content=content.read())


# TODO связь между sqlalchemy & pydantic


async def save_to_file_storage(recv_file) -> str:
    out_file_path = f"{random.randint(10 ** 8, 10 ** 9)}{recv_file.filename}"
    full_path = str(DIR) + "/FileStorage/" + out_file_path
    async with aiofiles.open(full_path, 'wb') as out_file:
        await recv_file.seek(0)
        while content := await recv_file.read(1024):  # async read chunk
            await out_file.write(content)  # async write chunk
    recv_file.file.close()
    return out_file_path
