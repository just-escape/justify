#!/usr/bin/env python3

import argparse
import csv
from math import ceil

import jinja2


def fill_templates(
    template_file, n_codes_per_template, codes, n_players, output_file_basename
):
    template_loader = jinja2.FileSystemLoader(searchpath=".")
    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template(template_file)

    n_output_files = len(codes) // n_codes_per_template

    for output_file_index in range(n_output_files):
        template_vars = {"n_players": n_players}
        for code_index in range(n_codes_per_template):
            template_vars[f"code_{code_index + 1}"] = codes[
                output_file_index * n_codes_per_template + code_index
            ]

        output_content = template.render(template_vars)

        output_file_name = f"{output_file_basename}_{output_file_index}.svg"
        print(f"Filling {output_file_name}")
        with open(output_file_name, "w+") as fh:
            fh.write(output_content)


def extract_codes(vouchers_file):
    codes = []
    with open(vouchers_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Code"]:  # can be an empty string in the last line
                codes.append(row["Code"])

    return codes


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("vouchers_file", type=str)
    parser.add_argument("n_players", type=str)
    parser.add_argument("template_file", type=str)
    parser.add_argument("--n-codes-per-template", type=int, default=12)
    parser.add_argument("--output-file-basename", type=str, default="COUPONS")

    args = parser.parse_args()

    expected_n_players = ["1", "2", "3", "4"]
    if args.n_players not in expected_n_players:
        print(f"Warning: n players is not one of {', '.join(expected_n_players)}")

    codes = extract_codes(args.vouchers_file)
    fill_templates(
        args.template_file,
        args.n_codes_per_template,
        codes,
        args.n_players,
        args.output_file_basename,
    )
    print("Done")
