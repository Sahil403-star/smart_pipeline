import click
from pipeline.pipeline import run_pipeline

@click.command()
@click.option('--pages', default=2, help='Number of pages to scrape')
def main(pages):
    print(f"Running pipeline for {pages} pages...")
    run_pipeline(pages)
    print("Pipeline execution completed!")

if __name__ == "__main__":
    main()