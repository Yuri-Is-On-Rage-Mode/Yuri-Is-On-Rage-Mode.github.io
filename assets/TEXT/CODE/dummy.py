import os
import json
from faker import Faker

# Create a directory for the dummy blog posts
blog_posts_dir = 'BlogPosts'
if not os.path.exists(blog_posts_dir):
    os.makedirs(blog_posts_dir)

# Initialize the Faker library for generating random content
fake = Faker()

def generate_blog_post(title):
    """Generate a blog post with a given title."""
    content = fake.text(max_nb_chars=2000)
    word_count = len(content.split())
    data = {
        "stars": fake.random_int(min=0, max=100),
        "pins": fake.random_int(min=0, max=100),
        "views": fake.random_int(min=0, max=1000),
        "likes": fake.random_int(min=0, max=100),
        "hates": fake.random_int(min=0, max=100),
        "length": word_count
    }
    post_dir = os.path.join(blog_posts_dir, title.replace(' ', '_'))
    if not os.path.exists(post_dir):
        os.makedirs(post_dir)
    
    # Write the blog content
    with open(os.path.join(post_dir, f'{title.replace(" ", "_")}.blog'), 'w') as f:
        f.write(content)
    
    # Write the metadata
    with open(os.path.join(post_dir, 'SomeData.json'), 'w') as f:
        json.dump(data, f, indent=4)
    
    return {
        "title": title,
        "stars": data["stars"],
        "pins": data["pins"],
        "views": data["views"],
        "likes": data["likes"],
        "hates": data["hates"],
        "length": data["length"]
    }

def generate_all_blog_posts(num_posts):
    """Generate a specified number of dummy blog posts and return their metadata."""
    posts_metadata = []
    for _ in range(num_posts):
        title = fake.sentence(nb_words=6).rstrip('.')
        post_metadata = generate_blog_post(title)
        posts_metadata.append(post_metadata)
    
    return posts_metadata

def save_posts_metadata(metadata):
    """Save all blog posts metadata to posts.json."""
    with open(os.path.join(blog_posts_dir, 'posts.json'), 'w') as f:
        json.dump(metadata, f, indent=4)

# Generate 20 dummy blog posts and save their metadata
posts_metadata = generate_all_blog_posts(20)
save_posts_metadata(posts_metadata)

print("Dummy blog posts created and metadata saved successfully.")
