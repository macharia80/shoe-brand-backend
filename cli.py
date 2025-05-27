# cli.py
import click
from database import SessionLocal, engine
from models import Base, Shoe

# Initialize database
def init_db():
    Base.metadata.create_all(bind=engine)

@click.group()
def cli():
    """Shoe Brand CLI Tool"""
    pass

@cli.command()
@click.argument('brand')
@click.argument('model')
@click.argument('size', type=float)
@click.argument('price', type=float)
def add(brand, model, size, price):
    """Add a new shoe to the database."""
    db = SessionLocal()
    try:
        shoe = Shoe(brand=brand, model=model, size=size, price=price)
        db.add(shoe)
        db.commit()
        db.refresh(shoe)
        click.echo(f"Added shoe: {shoe}")
    except Exception as e:
        db.rollback()
        click.echo(f"Error adding shoe: {e}")
    finally:
        db.close()

@cli.command()
def list():
    """List all shoes in the database."""
    db = SessionLocal()
    shoes = db.query(Shoe).all()
    for shoe in shoes:
        click.echo(shoe)
    db.close()

@cli.command()
@click.argument('shoe_id', type=int)
@click.option('--brand', help='New brand name')
@click.option('--model', help='New model name')
@click.option('--size', type=float, help='New size')
@click.option('--price', type=float, help='New price')
def update(shoe_id, brand, model, size, price):
    """Update a shoe by ID."""
    db = SessionLocal()
    shoe = db.query(Shoe).filter(Shoe.id == shoe_id).first()
    if not shoe:
        click.echo("Shoe not found.")
        return
    if brand:
        shoe.brand = brand
    if model:
        shoe.model = model
    if size is not None:
        shoe.size = size
    if price is not None:
        shoe.price = price
    db.commit()
    db.refresh(shoe)
    click.echo(f"Updated shoe: {shoe}")
    db.close()

@cli.command()
@click.argument('shoe_id', type=int)
def delete(shoe_id):
    """Delete a shoe by ID."""
    db = SessionLocal()
    shoe = db.query(Shoe).filter(Shoe.id == shoe_id).first()
    if not shoe:
        click.echo("Shoe not found.")
        return
    db.delete(shoe)
    db.commit()
    click.echo(f"Deleted shoe with ID {shoe_id}.")
    db.close()

if __name__ == '__main__':
    init_db()
    cli()