def manage_tags(existing_tags: dict, *simple_tags, **key_value_tags) -> dict:
    """
    Applies simple and key-value tags to an existing dictionary of tags.

    Args:
        existing_tags: The initial dictionary of tags.
        *simple_tags: Positional string arguments to be added as tags with a
                      value of 'true'. Duplicates should be ignored.
        **key_value_tags: Keyword arguments to be added or used to overwrite
                          existing tags.

    Returns:
        A new dictionary with all tags merged.
    """
    # TODO: Implement the tagging logic.
    # 1. Do not modify the original dictionary
    # 2. Process the 'simple_tags' (*args).
    # 3. Process the 'key_value_tags' (**kwargs).
    # 4. Return the new, merged dictionary.
    
    resultAux = existing_tags.copy()  # Create a copy to avoid modifying the original
    result = dict(existing_tags)
    for tag in set(simple_tags):
        result[tag] = 'true'
    result.update(key_value_tags)
    return result


manage_tags({"env": "prod", "tag2": "value2", "tag3": "value3"}, "web", "db", "web", owner="team-a", env="staging")