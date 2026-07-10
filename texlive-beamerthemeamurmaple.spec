%global tl_name beamerthemeamurmaple
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	A new modern beamer theme
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamerthemeamurmaple
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemeamurmaple.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemeamurmaple.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This Beamer theme is a suitable theme for my use of Beamer in applied
mathematics research. It meets my needs in my work. However, if you like
this theme, and if you want to ask for or make improvements, don't
hesitate to write to me!

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamerthemeamurmaple
%dir %{_datadir}/texmf-dist/tex/latex/beamerthemeamurmaple
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemeamurmaple/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemeamurmaple/README.md
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemeamurmaple/beamer-amurmaple-black.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemeamurmaple/beamer-amurmaple-blue.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemeamurmaple/beamer-amurmaple-doc.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemeamurmaple/beamer-amurmaple-doc.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemeamurmaple/beamer-amurmaple-green.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemeamurmaple/beamer-amurmaple-leftframetitle.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemeamurmaple/beamer-amurmaple-sidebar.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemeamurmaple/beamer-amurmaple-test.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemeamurmaple/logo.png
%{_datadir}/texmf-dist/tex/latex/beamerthemeamurmaple/beamerthemeAmurmaple.sty
