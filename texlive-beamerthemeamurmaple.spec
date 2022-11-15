Name:		texlive-beamerthemeamurmaple
Version:	64346
Release:	1
Summary:	A new modern beamer theme
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamerthemeamurmaple
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemeamurmaple.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemeamurmaple.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This Beamer theme is a suitable theme for my use of Beamer in
applied mathematics research. It meets my needs in my work.
However, if you like this theme, and if you want to ask for or
make improvements, don't hesitate to write to me!

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/beamerthemeamurmaple
%doc %{_texmfdistdir}/doc/latex/beamerthemeamurmaple

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
