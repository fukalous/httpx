import httpx


def test_all_imports_are_exported() -> None:
    included_private_members = ["__description__", "__title__", "__version__"]
    exported_members = [
        member
        for member in vars(httpx)
        if not member.startswith("_") or member in included_private_members
    ]
    assert sorted(httpx.__all__, key=str.casefold) == sorted(
        exported_members, key=str.casefold
    )
